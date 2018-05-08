import webapp2
import jinja2
import os
import logging
import shlex
import subprocess


jinja_environment = jinja2.Environment(autoescape=True,loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

# [START main_page]
class MainPage(webapp2.RequestHandler):
    def get(self):

    	template = jinja_environment.get_template('home.template')
    	self.response.out.write(template.render())


class ResultsPage(webapp2.RequestHandler):
    def get(self):
        logging.info('ProfilePage class requested')  
        latency_dict = {}
    	iplist=["35.196.56.100","8.8.8.8"]
		
        for ip in iplist:
			latency_dict[ip] = get_ping_time(ip)


    	self.template_values = {'latency_dict': latency_dict,}      
        
    	template = jinja_environment.get_template('results.template')
    	self.response.out.write(template.render(self.template_values))

    def get_simple_cmd_output(cmd, stderr=STDOUT):
    """
    Execute a simple external command and get its output.
    """
    	args = shlex.split(cmd)
    	return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]


	def get_ping_time(host):
    	host = host.split(':')[0]
   		cmd = "fping {host} -C 3 -q".format(host=host)
    	result = str(get_simple_cmd_output(cmd)).replace('\\', '').split(':')[-1].replace("n'", '').replace("-",'').replace("b''", '').split()
    	res = [float(x) for x in result]
    	
        if len(res) > 0:
        	return sum(res) / len(res)
    	else:
        	return 999999


# [START app]
app = webapp2.WSGIApplication([('/results', ResultsPage),('/', MainPage),], debug=True)
# [END app]
