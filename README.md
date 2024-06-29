# TextGenAI-on-CLI-with-gemini (Jynx)

![_f21c03eb-3920-44e5-b58f-59ba0e4a7a06](https://github.com/ImonChakraborty/jynx-gemini-context-CLI/assets/135951651/d8973ac2-c957-4a53-8510-92710588e5e9)


This is a command-line tool for generating text using generative AI. It leverages the power of Gemini 1.5 pro, a versatile language model trained by Google, to create natural language text. It uses a JSON file to keep track of the last 50 prompts and responses using a simple FIFO (First In First Out) technique, specifically a queue data structure to keep track of context while keeping the valuable token limit under control while conversing.

## Features

- **Text Generation**: Generate creative and coherent text based on prompts.
- **Usage of chat history**: Implementation of soft training data using chat history.
- **Context Awareness of last 50 conversations**: Adjust parameters like temperature and max length for varied output.
- **CLI Interface**: Easy-to-use command-line interface for quick and dynamic text generation with animation.

## Installation

1. Install Python (if not already installed).
2. Clone this repository:

   ```bash
   git clone https://github.com/ImonChakraborty/TextGenAI-on-CLI-with-gemini.git

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

## Before You start using it

- **Get your API key**: Go to https://aistudio.google.com/app/apikey and generate your api key.
- **Copy your API key**: Paste Your API key. ![image](https://github.com/ImonChakraborty/TextGenAI-on-CLI-with-gemini/assets/135951651/8f55955d-3865-4845-bb8e-1bc5dd743605)
- **Change the Location of the history JSON File**:

  1. For Windows:-

     ![image](https://github.com/ImonChakraborty/TextGenAI-on-CLI-with-gemini/assets/135951651/f77a55fa-4b59-4dd8-82b2-daea56392d30)

  2. For Linux:-

     ![Screenshot_29-Jun_13-46-46_10500](https://github.com/ImonChakraborty/jynx-gemini-context-CLI/assets/135951651/83030ed9-f8ba-4d3b-b4d3-1964bff55bbe)

     
- **Change it as per your use case**: ![image](https://github.com/ImonChakraborty/TextGenAI-on-CLI-with-gemini/assets/135951651/a3fa0843-4aa9-4fea-b1f5-8b04b273bf29)

## Usage

![image](https://github.com/ImonChakraborty/TextGenAI-on-CLI-with-gemini/assets/135951651/235a4200-51f2-45bb-940c-054e4081d1aa)

## To access it from Terminal in Windows

1. Open terminal:

     ```bash
     notepad $PROFILE
  
  if it is not available, refer to this video: https://youtu.be/E5tMwtoTd30?si=U7kVp21rw834Omqs

2. Paste this on $PROFILE:

     ```bash
     function jynx {python.exe "D:\programming\Python\TextGenAi.py" $args}

3. Save the powershell profile config and now you can use it on terminal itself:
      ![image](https://github.com/ImonChakraborty/TextGenAI-on-CLI-with-gemini/assets/135951651/b8f43461-a6a5-46cd-bb71-848ae052435e)

## To access it from Linux terminal

1. Open terminal / Konsole / Kitty / Alacritty / whatever you use

2. If you use bash:

      ```bash
      nano .bashrc

3. If you use zsh:

      ```bash
      nano .zshrc

4. Write:

      ```bash
      alias jynx="python Documents/TextGenAi.py"

5. Save & exit, now you can use it natively like this:
    ![image](https://github.com/ImonChakraborty/TextGenAI-on-CLI-with-gemini/assets/135951651/527ed327-efff-4862-9c86-45aad2412662)

## License
- This project is licensed under the MIT License. See the LICENSE file for details.




