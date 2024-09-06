from django.shortcuts import render
import random
from datetime import date
import os
from django.conf import settings

# Create your views here.
from django.http import HttpResponse

from django.views import View
    

class TestView(View):
    def get(self, request):
        # List of RGB colors
        colors = [
            'rgb(250, 51, 51)',  # Light red
            'rgb(66, 128, 227)',  # Light blue
            'rgb(196, 191, 81)',  # Light yellow
            'rgb(29, 97, 13)',  # Light green
        ]
        
        # Directory where images are stored
        # image_dir = os.path.join(settings.STATIC_ROOT, 'images')
        image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')

        # Get list of image file names in the directory
        images = [
            os.path.join('images', file) for file in os.listdir(image_dir)
            if file.endswith(('.jpg', '.jpeg', '.png', '.HEIC', '.JPG'))
        ]

        
        # Use today's date to get a consistent "random" value for the day
        today = date.today()
        # random.seed(today.toordinal())
        # random.seed(random.randint(0,1000))

        # Select a random color and image
        selected_color = random.choice(colors)
        selected_image = random.choice(images)
        
        messages = [
        """The happiness and excitement we shared tonight, that’s nothing but love. I’m dying for the day when you realise that you’re in love too. Come on love, Fall for me already."""

        , """No matter how much I say I love you, I’ll always love you more than that ❤️"""

        , """The kind of happiness I get by just thinking of spending a week with you is just so beautiful. One week or one month Saripodu naku. I want more more more time with you. Babe I promise to do whatever it takes to make us work and make sure we have all the time in the world. Can we just trust the process and always hold on to each other until then?"""

        , """You know why I love you? Cuz loving you feels so natural and effortless. It’s something I can’t help and it just has to happen. It makes me alive and happy. I don’t need a reason or a plan to love you. All I need is YOU. 
        I can’t tell you in words how much you mean to me. I really hope you feel the way I do, to truly understand this feeling."""

        , """Babe, every night I think how to tell you how I feel, but it’s so hard to put you in words because, I love you in ways I’ve never even thought of. I’ll still try my best to tell you however I can that I’m in love with you."""

        , """Babe, for the first time in my life, I don’t have to make an effort to be happy. All i need, is to be with you. Just YOU, is all I’ve ever wanted!"""

        , """It’s hard to wait for something that you know might never happen, but it’s impossible to give up when you know it’s everything you want. That’s the reason I’m never gonna give up on us."""

        , """My feelings are simple babe, I just want you to be happy and make you feel loved every single day. I’ll do my best and will never give up. I don’t know what else to say… just looking at you is making me so happy that I can’t explain. I love you more than you realise 🫶🏻"""

        , """Baby, i keep smiling just thinking abt you. You make me so so happppyyyyyy. I might not be perfect but I’m trying my hardest to love you better than anyone ever can and, hoping to make you as happppyyyyyy as you make me 🫶🏻"""

        , """I’ve spent so much time looking for someone like you and when I gave up, I found you. You are actually way better than what I was looking for and now I’m never gonna give up on you. Loving you is giving me so much happiness. I promise to never stop loving you. Not today, not tomorrow, not for the rest of my life. When you said that we’ll make it work, I felt so peaceful. Yes babe, we’re definitely gonna make it work. I Love you! ❤️"""

        , """No amount of time money and effort can ever be enough to tell you how much I love you. Baby I wake up at night, look at you, cuddle you and think how can I love you to make you happier than your happiest. I want to make you mine and only mine. Can I have you?"""

        , """I never knew i can be so happy by just knowing that you love me. Only thinking abt you is making me so happy. Love you tons ❤️"""

        , """Baby I might not be with you now But I promise to give you all my years very soon"""

        , """Us being apart is a fact. 
        We must not succumb to the darkness.
        We are sad but we gotta get through."""

        , """I love you more as each day passes by ❤️"""

        , """For the first time I’m craving for someone else’s company other than mine, loving someone else more than myself and willing to give up everything just to be with that person. It’s you honey. It’ll always be you!
        I love you babe ❤️"""

        , """Baby, I wanna do life with you. That’s all I want. Madhuri, I love you so much that I’d give up anything to be with you. Whatever life throws at us, I’m there for you and it’ll always be that way. Love you 🫶🏻"""

        , """Baby we will be back in each other’s arms soon enough.
        Hold onto our memories until then okay?
        And dont be sad missing me"""

        , """If only you could look at yourself from my eyes you’d know how special and amazing you are. I feel so lucky to have you babe. Very very lucky and I’m never gonna let anything come in our way! ❤️"""

        , """Baby I will always be there for you
        My hand will hold your hand forever
        All your problems are our problems love. Whatever life throws at us, we will face it together.
        I want you to feel loved, I want you to feel supported, I want you to know that I’ve always got your back."""

        , """You might be too far for my hands to hold yours, my lips to kiss you, my chest to hug you. But you are too near for my heart to love you… I’m always there with you baby!
        Just You and Me. Let’s do this life together.
        I love you so much! ♥️"""

        , """Baby I fell in love with you so fast and so hard, I was scared at first cuz it was toooo good to be true. But now I do know that I wanna fall in love with you even more. You make me the happiest man on earth. I love you more every day ❤️"""

        , """Babyyyyy you are my dream come true, the wish I made under the shooting stars, my whole heart. With you life is so so happy.
        Our relationship is so magical and full of love that I know, we can’t meet monthly or weekly but I can feel you everyyyy day and everyyyy night with me ❤️
        I love you so much baby! Forever and ever ❤️"""

        , """You are my everything and only you matter to me. Everything is worthless if you aren’t beside me. You make everything better ❤️"""

        , """In a few days we can kiss each other goodnight and cuddle to sleep ❤️"""

        , """After every goodnight, I wait for the next morning just so that I can see you ♥️"""

        , """I was a lil nervous on my way to pick you up, but once I saw you, everything got better. I’m not able to exactly express how I feel in words but Yesterday was the happiest I’ve been in a while. You made me really really happy. All my way to Hyd, I was thinking abt you and I couldn’t stop smiling. Can’t wait to see you again. Goodnighttttt 🤍"""

        , """Madhuri…. I wanna make you feel this way as long as I’m there. I’m hopelessly irretrievably in love with you and I can’t stop showing it to you. And the best part is, i wasn’t even looking for love when i found you."""

        , """I want you everywhere i go and every single second with me"""

        , """I have so many feelings in me that I can’t even express the slightest. I’m literally out of words love. I can’t stop smiling when I look at you. It doesn’t matter how many times I tell you, however I express, whatever I do, I’ll always feel it’s less. I’m lost in you, I’ve fallen for you and I’m in love with you. You are it. You just are it."""

        , """‘Perfect’, this is the only thing that i can think of when I wanna tell abt you to anyone"""

        , """I will come through, cause I only want you and I’ve fallen for you 👩‍❤️‍💋‍👩"""

        , """It’s like, even if I spend a whole day, a whole week, even a month I’ll still want you more and more. And still miss you the moment you leave. 😚"""

        , """Every night before sleeping, I think abt you and I try to tell you how much I’m in love with you and I can’t tell enough. Just a message notification from you makes me happy, that’s how much. I hope this message will brighten your day too. ❤️"""
        ]
        
        selected_message = random.choice(messages)

        # Pass the selected color and image to the template context
        context = {
            'bg_color': selected_color,
            'image_url': selected_image,
            'selected_message':selected_message
        }

        return render(request, 'mads/index.html', context)
