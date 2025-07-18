import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

MODEL_NAME = "gpt2"
DATA_PATH = "data/processed/mock_lyrics.csv"
TRAIN_FILE = "data/processed/train.txt"
OUTPUT_DIR = "models/checkpoints"

def prepare_dataset():
    import pandas as pd
    df = pd.read_csv(DATA_PATH)
    with open(TRAIN_FILE, "w", encoding="utf-8") as f:
        for lyric in df["lyrics"]:
            f.write(lyric.strip().replace("\n", "\n") + "\n\n")

from datasets import load_dataset
from transformers import DataCollatorForLanguageModeling

def train_model():
    tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)

    # Load data using 🤗 Datasets instead of deprecated TextDataset
    dataset = load_dataset('text', data_files={'train': TRAIN_FILE})
    dataset = dataset.map(lambda x: tokenizer(x['text'], truncation=True, padding="max_length"), batched=True)

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )

    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=10,
        save_total_limit=2,
        logging_dir="./logs"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset['train'],
        data_collator=data_collator,
    )

    trainer.train()
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)


if __name__ == "__main__":
    prepare_dataset()
    train_model()
