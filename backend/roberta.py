from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

contex = 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
question = 'Why is model conversion important?'

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def nlp_qna(contex, question):

# a) Get predictions

    QA_input = {
    'question': question,
    'context': contex,
    }
    res = nlp(QA_input)
    return res

res = nlp_qna(contex, question)
print(res)

# # b) Load model & tokenizer
# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
