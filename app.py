from flask import Flask

app = Flask(__name__)
#this __name is a special variable in python whose values are :
#1. main( if the current script is the main script
# 2. or name of the current script  (if the current script is a secondary script)

# note : scripts are also called modules


@app.route("/")
def hello_world():
  return "Hello yash"


print(__name__)
if __name__ == "__main__":  #checs if the current script is the main script
  app.run(host="0.0.0.0", debug=True)

  # host = 0.0.0.0 meas that we run this app on a local machine
  # debug = True means that any change in code is immediately reflected in the output page