The app is accessible at "https://skillsgit-e6v4fsbadldi4elghnfwon.streamlit.app" 
#Features and goals
This project is AI-powered club finder for new students or students in general
The project is structured in a multipage web-app powered by streamlit.
The first page enables students to explain their situation and if AI finds one or more fitting club it will recommend it to the student.
The second page contains 4 visualisation regarding to size, the recruiting statues and categories of the different clubs
#Structure and instructions
The app available online at the following link: "https://skillsgit-e6v4fsbadldi4elghnfwon.streamlit.app".
In case the app has not been used in long time please allow for some time for the initialisation.
In addition to the requirements file, there are five different files that are required to run the app.
App.py is the master file that is used to enable the navigation between the different pages and the initialization of the app.
Full.py is the file that creates the AI-powered club finder by being connected to OpenAI API on which shsg.clubs.keyword.json file is sent.
to enable the recommendation. Shsg.clubs.keywords.json is a compact file of shsg.clubs.json this transformation was required to not reach the token limit.
Clubsvisu.py powers the page which displays the visualization and filtering options according to the information found in the shsg.clubs.json

#instruction to run the code locally
Currently, the code is set up to run on the streamlit server if you want to run the code locally some change are required. 
If you want to run the code locally please first set your OpenAI API key as an environment variable in your device and link it accordingly.
By changing the path of the api key in the Full.py file to the path to the key on your device. For example for mac "api_key=os.getenv("OPENAI_API_KEY")"
Please also download all of the listed extensions in the requirements file.
Then run the app.py file and by writing "streamlit run "<<<path to the app.py file>>>"


