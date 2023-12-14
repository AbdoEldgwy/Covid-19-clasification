from flask import Flask, render_template,request,redirect, url_for
from keras.preprocessing import image
import numpy as np

def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    # img_array /= 255.0  # Normalize the pixel values to be between 0 and 1
    return img_array

def check_for_coronavirus(file):
    read_image = preprocess_image(file)
    from keras.models import load_model
    model = load_model(r'D:\Projects\test\model.h5')
    cheak_bool = model.predict([read_image])
    if int(np.round(cheak_bool[0][0],2))==1:
        return "COVID-19 Detection is : Positive"
    elif(int(np.round(cheak_bool[0][0],2))==0):
        return "COVID-19 Detection is : Negative"
    else:
        return "Something Error!"
        
#---------------------------------------

app = Flask(__name__)


@app.route("/")
def homepage():
  return render_template("homepage.html")

@app.route("/",methods=['POST'])
def my_form_post():
  mypath = request.form['file']
  result = check_for_coronavirus(mypath)
  return render_template("homepage.html",result=result)

  



#_________________________#
if __name__ == "__main__":
  app.run(debug=True,port = 9000)
  

