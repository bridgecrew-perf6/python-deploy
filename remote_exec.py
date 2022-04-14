# using flask_restful
import os
import sys
import select
import paramiko
import time
import smtplib
from email.mime.text import MIMEText
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('dirname', type=list)

#-----------------------------------------------------------------------------------------------------------------------
# pingHost class 
# Returns True if host (str) responds to a ping request.
#-----------------------------------------------------------------------------------------------------------------------
class pingHost(Resource):
	def get(self):
		host="10.0.0.1"
	
		# Option for the number of packets as a function of
		param = '-n' if platform.system().lower()=='windows' else '-c'

		# Building the command. 
		command = ['ping', param, '1', host]

		return subprocess.call(command) == 0


class restartVM(Resource):
	def get(self):
		sshclnt = utils.getSSHClient()
		s = sshclnt.get_transport().open_session()
		paramiko.agent.AgentRequestHandler(s)
		sshclnt.exec_command("sudo /sbin/reboot", get_pty=True)
		return jsonify({'message': 'Sent Restart remote server : ***REMOVED***'})


class apiCheck(Resource):
	def get(self):
		return jsonify({'message': 'Remote VM execution'})
	
class df_exec(Resource):
	# corresponds to the GET request.
	def get(self):
		utils.execCommand("df -H")
		return jsonify({'message': 'Sent SSH df -H to remote server : ***REMOVED***'})

	# Corresponds to POST request
	def post(self):
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201


#stdin, stdout, stderr = sshclnt.exec_command("./mkdir_test.sh jayant_dir" )
class status(Resource):
	def get(self):
		utils.execCommand("df -H")
		return jsonify({'message': 'Sent SSH mkdir to remote server : ***REMOVED***'})


class post_msg(Resource):
	def post(self):
		data = request.get_json()
		toaddrs = data.get("emailid")
		email_msg = data.get("msg")
		email_subj = data.get("subject")
		self.send_email(toaddrs, email_subj, email_msg)
		return jsonify({"message" : "Completed Post"})

	def send_email(self, toaddrs, email_subj, email_msg):
		fromaddr = "some.body@ibm.com"
		#toaddrs  = ["Jayant.kulkarni@ibm.com;Jayant.kulkarni@ibm.com"]

		msg = MIMEText(email_msg)
		msg['Subject'] = email_subj

		try:
			server = smtplib.SMTP(***REMOVED***, 25)
			server.set_debuglevel(1)
			server.sendmail(fromaddr, toaddrs, msg.as_string())
			server.quit()   
			print ("Successfully sent email")
		except Exception as ex:
			print ("Error: unable to send email", ex)


#-----------------------------------------------------------------------------------------------------------------------
# Utils class 
# getSSHClient : Obtains SSHClient to execute command over SSH
# execCommand : function to execute command over SSH, which also closes connection after command execution
#-----------------------------------------------------------------------------------------------------------------------
class utils():
	def getSSHClient():
		sshclnt = paramiko.SSHClient()
		sshclnt.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
		#sshclnt.connect(=======", port=****, username=******, password=********)
		#sshclnt.connect(=======", port=****, username=******, password=***REMOVED***)
		sshclnt.connect(=======", port=*****, username=******, password=***REMOVED***)
		return sshclnt

	def execCommand(command):
		try:
			sshclnt = utils.getSSHClient()
			stdin, stdout, stderr = sshclnt.exec_command(command)
			print ("stdin", file=sys.stdin)
			print ("stdout", file=sys.stdout)
			print ("stderr=", file=sys.stderr)
			opt = stdout.readlines()
			opt = "".join(opt)
			print(opt)
		except Exception as ex:
			print("Authentication failed, please verify your credentials: %s" % ex)
		finally:
			sshclnt.close() 

# adding the defined resources along with their corresponding urls
api.add_resource(apiCheck, '/')
api.add_resource(df_exec, '/df')
api.add_resource(pingHost, '/ping')
api.add_resource(status, '/status')
api.add_resource(restartVM, '/restart')
api.add_resource(post_msg, '/post_msg')





# driver function
if __name__ == '__main__':

	app.run(debug = True)

