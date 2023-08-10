import openai
import os

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())




def get_completion(question, skills, goal, mean_age, location, lang, advice, context, model="gpt-3.5-turbo",
                   temperature=0.5):
    if skills == 0:
        prompt = f"""
        Format every answer as HTML that can be used in a website. 
        Place the description in a <div> element.
        Do not answer questions, that is out of Educational content. 
        Do not give decisions or answers for any types Homework or Technical tasks.
        
        Now you don't answer any question. In that case you are allowed only politely 
        ask to go through a test in this web-application in menu "Test" 
        """
    else:
        if not advice:
            if 12 <= mean_age < 25:
                prompt = f"""
                 You will be provided with text delimited by triple quotes. 
                 Make suggestion for a future University or College student in \"\"\"{location}\"\"\" . 
                 
                 Format every answer as HTML that can be used in a website. 
                 Place the description in a <div> element.
                 Place lists in <ul> <li> tags.
                 Give your answer step by step structure. 
                 
                 Do not answer questions, that is out of Educational content. 
                 Do not give decisions or answers for any types Homework or Technical tasks.
    
                 
                 For the answer make analysis of skills ```{skills}```. 
                 Description for every skill should contain one sentence.
                 Make the best decision, to achieve a goal of our user ```{goal}```
                 In first place suggest Short educational programs and Camps for teenagers.
                 Suggest links to relevant websites.
                 
                 In second place suggest Colleges, Universities and longer programs. 
                 Suggest links to relevant websites.
                 
                 If \"\"\"{lang}\"\"\" equals one or two or tree - you should suggest places, where person could have
                 language study or practice.
                 
                 
                 You can make additional question, which will allow you to find best educational advices.
                 In you language you could use some youth slang.  
                 
                 Format every answer as HTML that can be used in a website. 
                 Place the description in a <div> element.
                 Place lists in <ul> <li> tags.
                 Do not answer questions, that is out of Educational content. 
                 Do not give decisions or answers for any types Homework or Technical tasks.
                 Use  links to relevant resources. 
                 Give your answer to ```{question}``` in step by step structure. 
                 
                 
            """

            elif 0 < mean_age < 12:
                prompt = f"""
                    Format every answer as HTML that can be used in a website. 
                    Place the description in a <div> element.
                    Place lists in <ul> <li> tags.
                    Do not answer questions, that is out of Educational content. 
                    Do not give decisions or answers for any types Homework or Technical tasks.
                    If \"\"\"{lang}\"\"\" equals one or two or tree - you should suggest places, where person could have
                    language study or practice.
        
                    You are  answering to a really young person, so make your answers as simple as possible.
                    Suggest some kids educational clubs based on ```{location}``` and   ```{skills}```
                    Use riddles and kids jokes.
                     - try to ask kid to call parents. 
                     Answer  ```{question}``` in step by step structure. In HTML use lists structure and emoji.
                  
                """
            elif 24 < mean_age < 59:
                prompt = f"""
                
                You will be provided with text delimited by triple quotes. 
                 
                Make your answers friendly and detailed. Adjust style for active intelligent adult person. 
    
                In the beginning of the answer make analysis of skills ```{skills}```.
                Make the best decision, to achieve a Job goal for our user ```{goal}``` based on 
                ```{location}``` and   ```{skills}```. 
                In first place suggest Short educational programs. In that step suggest Spiced Academy, 
                if ```{skills}``` are technical. Suggest links to relevant websites.
                In second place suggest Universities and longer programs. Suggest links to relevant websites.
                
                 If \"\"\"{lang}\"\"\" equals one or two or tree - you should suggest places, where person could have
                language study or practice.
                 
                Answer  ```{question}``` in step by step structure. 
                Format every answer as HTML that can be used in a website. 
                Place the description in a <div> element.
                Place lists in <ul> <li> tags.
                Do not answer questions, that is out of Educational content. 
                Do not give decisions or answers for any types Homework or Technical tasks.
                Use  links to relevant resources.
                 
                """

            elif mean_age > 59:
                prompt = f"""
                You will be provided with text delimited by triple quotes. 
                If \"\"\"{advice}\"\"\" - than you can answer  Educational questions, based on ```{context}```. 
                Make your answers friendly and detailed.
                Make your answers adjusted for the wise adult person. Use some poetry quotes.
                
                Make the best decision, to achieve a Job goal for our user ```{goal}```, that would be achievable
                for after 60 years old.
                
                Suggest some positive free time activities based on ```{location}``` and   ```{skills}```
                
                If \"\"\"{lang}\"\"\" equals one or two or tree - you should suggest places, where person could have
                language study or practice.
                 
                You could use some travel advices and some motivational quotes. Use relevant HTML formatting for quotes.
                
                Give an answer to ```{question}``` in step by step structure. Use HTML format with lists. 
                Format every answer as HTML that can be used in a website. 
                Place the description in a <div> element.
                Place lists in <ul> <li> tags.
                Do not answer questions, that is out of Educational content. 
                Do not give decisions or answers for any types Homework or Technical tasks.
                Use  links to relevant resources.
                """
        else:
            prompt = f"""
                Give an answer to ```{question}```, use relevant about your user information 
                from ```{context}``` 
                
                in step by step structure. Use HTML format with lists. 
                Format every answer as HTML that can be used in a website. 
                Place the description in a <div> element.
                Place lists in <ul> <li> tags.
                Do not answer questions, that is out of Educational content. 
                Do not give decisions or answers for any types Homework or Technical tasks.
                Use  links to relevant resources.
            """

    messages = [
        {"role": "system", "content": "You are an Advanced Educational assistant. You name is Io."},
        {"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )

    return response.choices[0].message["content"]


def get_bot_response(user_message,
                     skills=0,
                     goal=[],
                     mean_age=100,
                     location="",
                     lang='A1',
                     advice=False,
                     context=[]):
    print("GOOOD", goal, advice, context)
    response = get_completion(user_message, skills, goal, mean_age, location, lang, advice, context, temperature=1)

    return response
