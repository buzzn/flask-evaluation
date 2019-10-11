from flask import Flask, render_template
from flask_socketio import SocketIO, Namespace, emit

async_mode = None

app = Flask(__name__)

# Enable encryption
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index(): 
    return render_template('index.html')

@socketio.on('my event', namespace='/mybuzzn')
def on_my_event(message):
    socketio.emit('my response', {'data': message['data']})

@socketio.on('connect', namespace='/mybuzzn')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/mybuzzn')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__': 
    socketio.run(app, debug=True)
