# Autocomplete API

Autocomplete API that helps users searching for apps by
their name. When writing the name of an app, the possible results should be shown to
the user. For example, if the user is inputting *Fac*, two possible choices are
*Facebook* and *Facebook Lite*.

The microservice/web service receives as input a
user query, ask the autocomplete system for the possible results and send them back.


## Deployment

**Building from source**

Clone this repository
```bash
git clone https://github.com/AndreMPCosta/AptoideChallenge.git
cd AptoideChallenge
```

Inside the project directory, run the command below. This will do all the steps necessary to build and run as a Docker Image.
```bash
sudo bash start.sh
```

It is configured to run on the default port(5000), you can change that on the Dockerfile and on start.sh if you prefer another port.

## Usage
The app is loading the 6500 titles csv file. 

You can use *Postman* or your *Browser* to make a simple query, since the GET verb is being used on this case.

**Sample call:**
```
http://localhost:5000/query/your_prefix_here
```
**Example:**
```
http://localhost:5000/query/fac
```
You should get this response as JSON:
```json
{
results: [
"facebook",
"facebook lite",
"facebook pages manager",
"facebook groups",
"facebook apps market",
"facebook video download",
"face changer",
"face changer 2",
"face time calling guide",
"face swap",
"faceapp",
"facelock for apps",
"facelook for facebook",
"facetune",
"faceswap face swap live"
]
}
```
