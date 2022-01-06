# SFHacks

This GitHub repo contains all the necessary build files for the club site [SFHacks](https://sfhacks.club). Inside of this repo you will find the directories
- ```templates```, which houses all the HTML files used to display the content
- ```static```, which contains all images, favicons, and necessary static files to build this website
- ```main.py```, the root file of this repository which has app routing using Flask and necessary Python code.


**Note that this project utilizes several javascript and CSS libraries, all of which can be found from [CDNJS](https://cdnjs.com).**


## Python

The Python file that is used as the root file in this project contains a module ```Flask``` for app routing. Basic flask routing serves this purpose of rendering HTML. 
Below is a demonstration of rendering HTML using Flask and its application into this project.

```python
from flask import Flask, render_template, send_file

#the main route of the app
@app.route('/')
#function syntaax
def homePage():
  return render_template("index.html")
 
 @app.route('/favicon.ico')
 def favicon():
  return send_file("static/assets/favicon/logo.png")
  
```

Flask searches for the ```templates``` folder, so no specification is needed when passing the file name into the ```render_template``` function.

### Favicon Routing
The favicon routing deals with the extension (subpage) favicon.ico. When I pass the /favicon.ico route into the web browser, the file immediately is rendered. This is especially useful when passing this route into the ```<link>``` tags of HTML.


## HTML

### Spectre.css

This project heavily utilizes the library [SPECTRE.CSS](https://picturepan2.github.io/spectre/index.html). Documentation can found by clicking the link. 

Spectre.css is a CSS library similar to that of Bootstrap. However, the styling is different and more features are added to this library. 

### FullPage.js

Fullpage.js can create beautiful snap windows which make scrolling visually easier and more efficient. Documentation can be found [here](https://alvarotrigo.com/fullPage/).
Intializing fullpage is simple and the implementation can be found below: 

```html
<div id="fullpage" style="margin-left: 5vh">
  <div class="section">
  </div>
</div>
````

The class section declares a page and the margin-left is **only** for styling purposes. The fullpage class on the parent ```<div>``` intializes fullpage. Below is the javascript implementation of fullpage.

```javascript
new fullpage('#fullpage', {
  //options here
  autoScrolling:true,
  scrollHorizontally: true
});
```

#### Summary
The two libraries used in this project are Spectre.css and Fullpage.js. Implementations can be found in the code snippets as well as the repo itself.

### Background
The background of this site is a gradient. The implementation of how to do this is below:

```css
.section {
  background-size: cover;
  }
body {
  background-image: linear-gradient(to right, #f3f3ff, #daf9ff)
}
```
This utilizes linear gradient and hex colors are specified within the code snippet.




