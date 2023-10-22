from flask import Flask, request, jsonify
import redis
import requests

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    key = request.form['key']

    pod_name = redis_client.get(key)
    
    if pod_name:
        pod_name = pod_name.decode('utf-8')
        
        # Route traffic to the 'dynamic-pods' service with the selected pod_name
        response = requests.get(f"http://{pod_name}.default.svc.cluster.local", params={'key': key})
        
        # Return the response from the specific pod
        return response.text, response.status_code
    else:
        return "Not Found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)









#from flask import Flask, request, jsonify
#import redis

#app = Flask(__name__)
#redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

#@app.route('/authenticate', methods=['POST'])
#def authenticate():
 #   key = request.form['key']
  #  pod_name = redis_client.get(key)
    
   # if pod_name:
    #    return jsonify({'pod_name': pod_name.decode('utf-8')})
    #else:
     #   return "Not Found", 404

#if __name__ == '__main__':
 #   app.run(host='0.0.0.0', port=80)
