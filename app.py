from flask import Flask, render_template, request
import config
import aicontent

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/product-description', methods=["GET", "POST"])
def productDescription(): #product description

    if request.method == 'POST':
        query = request.form['productDescription']
        openAIAnswer =   aicontent.aicontent(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('product-description.html', **locals())



@app.route('/job-description', methods=["GET", "POST"])
def jobDescription(): #job description

    if request.method == 'POST':
        query = request.form['jobDescription']
        openAIAnswer =   aicontent.aicontent(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('job-description.html', **locals())



@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas(): #tweet ideas

    if request.method == 'POST':
        query = request.form['tweetIdeas']
        openAIAnswer =   aicontent.aicontent(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('tweet-ideas.html', **locals())



@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails(): #coldemails

    if request.method == 'POST':
        query = request.form['coldEmails']
        openAIAnswer =   aicontent.aicontent(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('cold-emails.html', **locals())



@app.route('/social-media', methods=["GET", "POST"])
def socialMedia(): #socialmedia

    if request.method == 'POST':
        query = request.form['socialMedia']
        openAIAnswer =   aicontent.aicontent(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('social-media.html', **locals())


@app.route('/business-pitch', methods=["GET", "POST"])
def businessPitch(): #Marketing 

    if request.method == 'POST':
        query = request.form['businessPitch']
        openAIAnswer =   aicontent.aicontent(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('business-pitch.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas(): #youtube

    if request.method == 'POST':
        query = request.form['videoIdeas']
        openAIAnswer =   aicontent.aicontent(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"])
def videoDescription(): #videodesc

    if request.method == 'POST':
        query = request.form['videoDescription']
        openAIAnswer =   aicontent.aicontent(query)
        prompt = 'AI Suggestions for {} are:'.format(query)

    return render_template('video-description.html', **locals())










if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
