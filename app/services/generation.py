import torch
import re
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
)


def generation(rubrics, name_org, org_address, rating):
    """ Travel time prediction """
    
    tokenizer = AutoTokenizer.from_pretrained("./model/train-model-2")
    model = AutoModelForCausalLM.from_pretrained(
        pretrained_model_name_or_path="./model/train-model-2",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    # Перемещение модели на GPU или CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    rubrics = str(rubrics)
    name_org = str(name_org)
    org_address = str (org_address)
    rating = str (rating)
    input_text = f"rubrics = {rubrics}\nrating = {rating}\nReview: "
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    output = model.generate(
        **inputs,
        max_length=60,
        temperature=0.8,
        no_repeat_ngram_size=2,
        do_sample=True,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,  # Установка токена конца последовательности
        pad_token_id=tokenizer.eos_token_id,  # Использовать тот же токен для паддинга
        early_stopping=False,  # Раннее завершение на токене конца
        top_k=30,         # Уменьшаем количество рассматриваемых верхних k слов
        top_p=0.8,        # Уменьшаем "ядерность" распределения
    )

    for i, sequence in enumerate(output):
        generate_text = tokenizer.decode(sequence, skip_special_tokens=True)
        raw_text = re.findall(r'(?<=Review:  ).*', generate_text)[0]
        
    result = raw_text
    return result