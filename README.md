The app is accessible at "https://skills-public-gugqf5h85ur8grmnv7phms.streamlit.app" 

##Features and goals

This project is an AI-powered club finder for new students or students in general.
The project is structured in a multipage web app powered by Streamlit.
The first page allows students to explain their situation, and if AI identifies one or more suitable clubs, it will recommend them to the student.
The second page contains 4 visualizations regarding size, the recruiting statute, and categories of the different clubs

##Structure and instructions

The app is available online at the following link: "https://skills-public-gugqf5h85ur8grmnv7phms.streamlit.app".
If the app has not been used in a long time, please allow some time for initialization.
In addition to the requirements file, five different files are required to run the app.
main.py is the master file used to enable navigation between different pages and initialize the app.
OPENAIAPI.py is the file that creates the AI-powered club finder by connecting to the OpenAI API, to which the shsg.clubs.keyword.json file is sent to enable recommendations. Shsg.clubs.keywords.json is a compact file of shsg.clubs.json. This transformation was required to avoid reaching the API token limit. Clubsvisu.py powers the page, which displays the visualization and filtering options based on the information found in the shsg.clubs.json file and is laid out accordingly. Overall, the app utilizes the Streamlit infrastructure to display information in a user-friendly manner.

##Instruction to run the code locally

Normally, there is no need to run it locally as running it locally would provide the same outcome as running it on the server (current status).
Currently, the code is set up to run on the Streamlit server. To run the code locally, some changes are required. 
If you want to run the code locally, please first set your OpenAI API key as an environment variable in your device and link it accordingly.
By changing the path of the API key in the OPENAIAPI.py file to the path to the key on your device. For example for mac "api_key=os.getenv("OPENAI_API_KEY")"
Please also download all of the listed extensions in the requirements file.
Then run the main.py file and by writing "streamlit run "<<<"path to the main.py file">>>"
If you want to run the app locally, please send an email to nilsmichel.nguyen@student.unisg.ch so I can provide you with the OpenAI API key, as it is recommended not to share it on a public git.



