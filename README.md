# DelveiBot
A Chatbot allow communication between who have lost someting and who found someting.

## Getting Started
### Requires
* Line developer account
* ngrok (localhost)
* Dialogflow
* mongoDB
* Flask


### Install library
```shell
$ pip3 install -r requirements.txt 
```

### Configulation
```cd app/config.py```
| variable | Description |
| ------ | ----------- |
| root_path  | URL path for accessing route. |
| image_path | Relative path of image folder. |
| credential_path |  credentrial Dialogflow key. |
| project_id | Project ID of Dialogflow agent. |
| Channel_access_token | Your own Line Channel access token |
| Channel_secret | Your own Channel secret |

### How to run
* ```cd app/``` then run code below.
```shell
$ python app.py 
```
* open ngrok ```ngrok.exe``` then run code below.
```shell
$ ngrok http port 3000
```
* copy url path and connect with line webhook. For example ```https://911f1c3208b9.ngrok.io```

## Results
![](doc/Results.png)
![](doc/delveibot_gif.gif)

## Reference
- Map from princess chulabhorn science high school mukdahan (my high school)
