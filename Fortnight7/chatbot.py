import flask
import tkinter as tk

from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import tensorflow as tf
from transformers import DataCollatorForSeq2Seq
from datasets import load_dataset
from transformers import create_optimizer
import tensorflow as tf
#model_name = "facebook/blenderbot_small-90M"
class chatbot:
    
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = TFAutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.data_collator = DataCollatorForSeq2Seq(self.tokenizer, model=self.model, return_tensors="tf")
        #self.dataset = load_dataset(dataset,split="train")
        self.NEXT_UTTERAN = ""
        
    def train_model(self):
                # Shuffle the dataset
        shuffled_dataset = self.dataset.shuffle(seed=42)
                # Select a small sample
        sample_size = 10
        sample_dataset = shuffled_dataset.select(range(sample_size))
        tokenized_dataset = sample_dataset.map(self.preprocess_function, batched=True)
        tokenized_dataset_no_text = tokenized_dataset.remove_columns(["conversations"])
        tf_train_dataset = self.model.prepare_tf_dataset(
            tokenized_dataset_no_text,
            collate_fn=self.data_collator,
            shuffle=True,
            batch_size=8,
        )
        num_train_epochs = 8
        num_train_steps = len(tf_train_dataset) * num_train_epochs

        optimizer, schedule = create_optimizer(
            init_lr=5.6e-5,
            num_warmup_steps=0,
            num_train_steps=num_train_steps,
            weight_decay_rate=0.01,
        )

        loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

        self.model.compile(optimizer=optimizer,loss=loss)
        
        self.model.fit(tf_train_dataset, epochs=num_train_epochs)
        
        
    def preprocess_function(self, example):
        input_texts = []
        target_texts = []

        for curr_conv in example['conversations']:

            prompt = ""

            for idx in range(len(curr_conv)-1):
                prompt += curr_conv[idx]["from"] + " "  #should be either "system" or "human" - theoretically could be an earlier "gpt" if there is more than one gpt response
                prompt += curr_conv[idx]["value"] + " " #associated prompt

            response = curr_conv[-1]["value"] #should be the gpt response

            input_texts.append(prompt)
            target_texts.append(response)

        # Tokenize inputs and targets
        model_inputs = self.tokenizer(input_texts, max_length=512, truncation=True, padding='max_length')
        labels = self.tokenizer(target_texts, max_length=512, truncation=True, padding='max_length')
        #move the target tokens into the model_inputs as the "decoder_input_ids"
        model_inputs["decoder_input_ids"] = labels["input_ids"]
        model_inputs["labels"] = labels["input_ids"]

        return model_inputs

    def chatbot_response(self, user_input):
        self.NEXT_UTTERAN += ("__start__" + user_input + "__end__")
        inputs = self.tokenizer([user_input], return_tensors="tf")
        reply_ids = self.model.generate(input_ids=inputs["input_ids"],attention_mask=inputs["attention_mask"])
        decoded_reply = self.tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
        
        self.NEXT_UTTERAN += ("__start__" + decoded_reply + "__end__")
        
        return decoded_reply

    def run_gui(self):
        self.root = tk.Tk()
        self.root.title("Chatbot")

        # Create the chatbot's text area
        self.text_area = tk.Text(self.root, bg="white", width=100, height=20)
        self.text_area.pack()

        # Create the user's input field
        self.input_field = tk.Entry(self.root, width=50)
        self.input_field.pack()

        # Create the send button
        self.send_button = tk.Button(self.root, text="Send", command=lambda: self.send_message())
        self.send_button.pack()
        
        self.root.mainloop()

    def send_message(self):
        # Get the user's input
        user_input = self.input_field.get()

        # Clear the input field
        self.input_field.delete(0, tk.END)

        # Generate a response from the chatbot
        response = self.chatbot_response(user_input)

        # Display the response in the chatbot's text area
        self.text_area.insert(tk.END, f"User: {user_input}\n")
        self.text_area.insert(tk.END, f"Chatbot: {response}\n")
        
        print(self.NEXT_UTTERAN)

        
chat = chatbot("facebook/blenderbot_small-90M")

chat.run_gui()