from new_flask_web_app.flask_config import app
from flask import request,render_template
from new_flask_web_app.empinfo import Employee

emplist = []

def checkempinfo(formdata):     #either -- dict:errors --> emp:noerrors
    eid = formdata.get('empid')
    name = formdata.get('empname')
    eage = formdata.get('empage')
    gen = formdata.get('empgen')
    city = formdata.get('ecity')
    sal = formdata.get('empsal')
    email = formdata.get('empemail')
    role = formdata.get('emprole')
    skills = formdata.getlist('empskills')
    hobbies = formdata.getlist('emphob')

    errors = {}  # when dict will have pair ?? --?
    if len(eid)<=0 or len(name)<=0 or   len(eage)<=0 or len(gen)<=0 or len(city)<=0 or len(sal)<=0 or len(email)<=0 or len(role) <= 0 or len(skills) <= 0  or len(hobbies) <= 0:
        errors["ALL"] = "Mandatory fields --> needs to be filled..!"
        return errors

    if len(eid)<=0 or int(eid)<=0:
        errors["EMPID"] = "Invalid Emp Id"
    if len(name)<2 :     #none --> empty -->True
        errors["EMPNAME"] = "Invalid Emp NAME"
    if len(eage)<=0 or int(eage)<22 or int(eage)> 100:
        errors["EMPAGE"] = "Invalid Emp Age"

    if not errors:      # no pairs inside dict--> no error
        return Employee(eid, name, eage, gen, city, sal, email, role, skills, hobbies)      # empinstance
    return errors       # dict

@app.route("/")     #http://localhost:5000/
def login_page():
    return render_template('login.html')

@app.route("/signup",methods = ["GET","POST"])      # register link thru --> post--> register form submit la
def user_register():
    msg = ""
    if request.method=='POST':              # register form thru
        formdata = request.form             # form -- post madhn baher kadla
        result = checkempinfo(formdata)     #method la pass -- cross check -- data valid ahe ka
        if type(result)==dict: # means errors
            return render_template('register.html',data=formdata,resp = msg,emps = emplist,errors=result)
        else:
            emplist.append(result)
            msg = "Emp Information Recorded"
            return render_template('register.html',resp = msg,emps = emplist,data={})

    return render_template('register.html', resp='', emps=emplist,data={})


if __name__ == '__main__':
    app.run(debug=True)
