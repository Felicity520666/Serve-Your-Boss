# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Milo")
define k = Character("Kirill", color="#00FF83")
define b = Character("Man-Eating Beast", color="#9DF179")
## Small transforms that place images at the left and right and make them smaller.
# Using xalign/yalign keeps placement consistent across resolutions.

label start:
    play music "whimsical-children-pizz-sneaky-cartoon-ending-20-sec-409321.mp3"
    scene magic town with fade
    pause 1.0
    play sound "hi-413164.mp3" volume 8.0
    show happy at right with dissolve
    m "Oh hello there! Welcome to our Magic Town!"
    m "My name is Milo!"
    m "This is a realm of wonder, filled with joy and enchantment!"
    m "For generations upon generations, we have lived here peacfully."
    m "There's nothing to worry about, nothing to fear..."
    play sound "woman-sigh-101931.mp3" volume 3.0
    show sad ghost at right with dissolve
    m " Well, almost..."
    hide sad ghost with dissolve
    show happy at right with dissolve
    m "But, uh, do you want to know? I mean, you just got here — I don't want to freak you out or anything!"
    menu:
        "Yes, tell me, I want to know more about this place.":
            show scared at right with dissolve
            m "Okay then, let me teel you all about it."
            play sound "woman-sigh-101931.mp3" volume 3.0
            m "It surely is a long story..."
            hide scared with dissolve
            jump story
        "No, it's okay. I don't want to hear about it.":
            show happy at right with dissolve
            play sound "woman-sigh-101931.mp3" volume 3.0
            m "Yeah, that's probably for the best!"
            m "It's always better to focus on the positive things in life, right?"
            m "So come on, let me show you around!"
            jump visit
label visit:
    scene pond with fade
    m "And now, let my show you the Holy Pond!"
    m "It's said that anyone who drinks from its waters will be blessed with good fortune and happiness."
    m "I believe that's why our Magic Town is so joyful and happy..."
    play sound "woman-sigh-101931.mp3" volume 3.0
    m "Well..."
    m "Sorry, let's continue our tour!"
    m "Next, I want to take you to the Melody Meadow!"
    m "It's a place where the flowers bloom in vibrant colors and the air is filled with the sweet sound of music."
    m "You can even hear..."
    play sound "real-yaoi-fangasm6-104926.mp3" volume 2.0
    show angry at left with dissolve
    k "Milo! What are you doing here?!"
    k "Do you know what time it is!"
    m "Kirill? What do you mean?"
    m "It's..."
    m "Oh no!"
    hide angry with dissolve
    show urging at left with dissolve
    k "No time to waste Milo! You have to prepare the dinner! Now!"
    m "But Kirill, what about our guest?"
    hide urging with dissolve
    show angry at left with dissolve
    k "What! You haven't tell our guest about the Man-Eating Beast?"
    m "Well, I thought it might be better not to scare our precious guest..."
    hide angry with dissolve
    show urging at left with dissolve
    k "If you don't quickly prepare his dinner, the Beast will be furious!"
    m "Fine, but first, let me at least explain the whole thing to our guest..."
    hide urging with dissolve
    jump story
label story:
    scene magic town with fade
    play music "intro_290125_vip-294096.mp3" 
    show happy at right with dissolve
    m "Long, long ago, in my grandparents' day, our town was a tiny world alive with charming little fairies and playful spirits."
    m "For a long time, we lived in peace."
    scene monster with fade
    play sound "deep-sea-monster-roar-329857.mp3"
    m "But then, a great monster appeared — one who despised our kind."
    m "We called him the Man-Eating Beast, for each day he would claim one of us as his meal."
    m "To keep us safe, we decided to take turns preparing his dinner, so that he would not harm us."
    scene hazy bg with fade
    m "He resides in the Gloomfang Bay, not far from our wonderland..."
    play sound "woman-sigh-101931.mp3" volume 3.0
    scene magic town with fade
    show sad ghost at right with dissolve
    m "And today, it's my turn to serve his dinner..."
    show mad at right with dissolve
    m "The Man-Eating Beast no longer devours us, but he still wanders in and trashes our homes, stealing the peace we once knew."
    hide mad with dissolve
    show sad ghost at right with dissolve
    m "It truly is a shadow over our little town."
    hide sad ghost with dissolve
    show mad at right with dissolve
    m "But I know there's a way to end him — I learned it while serving his meal."
    hide mad with dissolve
    show think at right with dissolve
    m "When I last served his meal, he ate with a terrible hunger, shoveling food into his mouth as if he couldn't stop."
    m "If I slipped poison into his dinner tonight, he wouldn't notice, and we could finally live in peace."
    hide think with dissolve
    show sad ghost at right with dissolve
    m "But I am the only one who knows this."
    m "Yet that would be monstrous. I am mild-tempered and cannot kill in cold blood."
    show scared at right with dissolve
    m "You've just arrived, but I need your counsel — our people will shrink from it. Tell me, my dear guest, should I do it?"
    hide scared with dissolve
    menu:
        "Of course! You must save your town. Be brave and do what's necessary.":
            jump poison
        "Sticking to the old ways is the safest... Just serve dinner as usual.":
            jump dinner
label scene_loop:
    # Loop through scenes 1-5 with 0.1 second pauses
    $ i = 0
    while i < 6:
        scene 1
        pause 0.05
        scene 2
        pause 0.05
        scene 3
        pause 0.05
        scene 4
        pause 0.05
        scene 5
        pause 0.05
        $ i += 1
    return

label poison:
    play music "mistery-intro-285699.mp3" fadein 1.0
    show happy at right with dissolve
    m "Really...You think I should do that?" 
    m "Hmm... I mean... I know that's the best way to keep everyone safe."
    show scared at right with dissolve
    m "So, although I am really afraid, I trust your judgment!"
    show happy at right with dissolve
    m "Come with me quickly, we must prepare the special dinner!"
    hide happy with dissolve
    scene add with fade
    play sound "bubbles-003-6397.mp3" volume 2.0
    pause 1.5
    m "It's almost ready..."
    pause 1.5
    stop sound
    m "All done... Now, time to serve it to the Beast..."
    scene walking with fade
    play sound "woman-sigh-101931.mp3" volume 3.0
    pause 3.5
    play sound "game-eat-sound-83240.mp3" volume 3.0
    scene eat with dissolve
    pause 2.0
    scene notgood with fade
    play sound "monster-15-337349.mp3" volume 3.5
    b "GROARRR!!! Why... Why do I feel so SICK..."
    b "What the heck did you put in my dinner?!"
    play sound "heavy-girl-breathing-149496.mp3" volume 2.0
    b "Why am I so dizzy after eating that?!"
    show scared at left with dissolve
    m "Oh my! The poison is working!!"
    m "I... I can't believe I'm murdering a living being..."
    m "I'm a murderer..."
    m "Oh no... I am killing a creature!"
    m "Please forgive me..."
    m "I am so cruel..."
    hide scared with dissolve
    b "Say what? You added poison in to my dinner?!"
    play sound "low-no-82600.mp3" volume 2.0
    b "NOOOOOO!"
    show sad ghost at left with dissolve
    m "Sorry, but I had to do it for the sake of my town..."
    m "You really made our lives suffer..."
    hide sad ghost with dissolve
    show happy at left with dissolve
    m "So I guess I did the right thing..."
    m "I hope you can rest in peace..."
    m "And be a good soul in the afterlife."
    scene death with fade
    pause 0.1
    play sound "deep-sea-monster-roar-329857.mp3"
    b "Ahhhhhhhhh..."
    pause 2.0
    scene dead
    pause 1.0
    m "So, that's the end of the Man-Eating Beast..."
    m "And I decide to tell everyone the truth about what happened."
    m "I hope they'll fell happy that our Magic Town is finally safe again."
    jump ending
label dinner:
    play music "magic-mystery-harry-potter-music-320643.mp3" fadein 1.0
    show happy at right with dissolve
    m "Yeah, you're right..."
    show sad ghost at right with dissolve
    m "I guess it's better to stick to what we know."
    show happy at right with dissolve
    m "I mean, nobody's been eaten in years, right?"
    show sad ghost at right with dissolve
    m "So, I guess poisoning him is just a silly idea after all..."
    hide sad ghost with dissolve    
    show scared at right with dissolve
    m "Oh, no time to waste! Come with me quickly, we must prepare his dinner!"
    m "If I don't serve it in time, he will definitely get angry and might do something terrible!"
    scene kichen with fade
    play sound "flowing-water-345171.mp3" volume 2.0
    pause 1.5
    show happy at right with dissolve
    m "Almost ready!"
    m "You know what? I am the greatest chef in the whole Magic Town!"
    m "THE BEST! At least, that's what my mom says..."
    show scared at right with dissolve
    m "I have confidence!!!"
    hide scared with dissolve
    show happy at right with dissolve
    m "I added an extra special ingredient to make it extra tasty!"
    m "I think it's the most delicious thing in the world!"
    m "I just can't stop thinking how fantastic it is!"
    hide happy with dissolve
    show scared at right with dissolve
    m "BEST DISH IN THE WORLD!!!!!"
    hide scared with dissolve
    show happy at right with dissolve
    m "Hehe, sorry, I got a bit carried away..."
    m "I just figured that dish out myself recently, and I'm so proud of it!"
    m "The beast is going to be the second one to try it after me..."
    hide happy with dissolve
    show sad ghost at right with dissolve
    m "I hope he doesn't hurt me..."
    hide sad ghost with dissolve
    show scared at right with dissolve
    m "Everytime I think of the Man-Eating Beast, I get chills down my spine..."
    play sound "microwave-timer-117077.mp3" volume 1.5
    hide scared with dissolve
    show sad ghost at right with dissolve
    m "Oops! Sounds like the dish is ready... Looks like I'll have to go face the reality now..."
    hide sad ghost with dissolve
    show happy at right with dissolve
    m "Wish me luck!"
    scene walking with fade
    play sound "woman-sigh-101931.mp3" volume 3.0
    pause 3.5
    play sound "game-eat-sound-83240.mp3" volume 3.0
    scene eat with dissolve
    pause 2.0
    play music "happy-kids-333364.mp3" fadein 0.5
    play sound "wow-423653.mp3"
    call scene_loop
    play sound "wow-423653.mp3" 
    scene glad with fade
    play sound "water-splash-46402.mp3" volume 3.0
    pause 1.0
    scene pleasent with dissolve
    b "Oh my god… what is happening inside my mouth right now? This flavor—this overwhelming wave of celestial beauty—it's unreal! What is this dish called? Tell me immediately!"
    play sound "oh-my-gosh-did-you-hear-that-322658.mp3" volume 3.0
    m "Oh my gosh did you hear that!"
    m "The Man-Eating Beast loves my cooking!"
    m "It's called the Celestial Blossom Essence of the Golden Boar."
    play sound "wow-male-voice-65342.mp3" volume 3.0
    b "Wow!"
    b "Celestial—what? My god, the name alone sounds like a miracle. And it tastes even more divine than it sounds."
    b "The fragrance of these blossoms is exploding across my tongue like a paradise unfolding under moonlight."
    b "How is it so pure? So radiant? So impossibly silky?"
    b "I swear I'm stepping into a blooming kingdom made entirely of petals and starlight!"
    m "I'm glad you like it."
    b "Like it? LIKE IT? This masterpiece is reshaping my entire understanding of beauty and flavor."
    b "t's so delicious it's almost immoral!!!"
    b "The aroma is pristine, the texture is liquid velvet, the taste is pure enchantment."
    b "How did anyone create something this magnificent? This isn't cooking—this is heavenly engineering!"
    m "Wow... You're basically a Michelin poet at this point."
    b "Shush! I'm not done. This dish is transforming my soul. I feel like I'm becoming a flower myself—gentle, glowing, impossibly pure."
    b "f I sprout petals right now, do not be surprised..."
    m "Hehe...I swear you just described food better than most people describe their life goals."
    b "This food has awakened some soft, secret place inside me that I didn't even know existed."
    m "Oh, okay... Um... Do you need a moment?"
    b "A moment? I need an entire journey!!!"
    b "I'm overflowing with energy. I have to dive into the bay and swim until the waves calm me down, before this dish completely overwhelms my mortal body."
    m "Thank you for your accom..."
    scene enter
    play sound "water-splash-02-352021.mp3"
    m "Oh he's gone."
    play music "fun-435786.mp3"
    scene fish with dissolve
    b "What?! There are fish in the bay?!"
    b "I've never noticed that before!"
    b "Fish! DELICIOUS FISH!"
    b "So there are fish in the bay, I can just eat them as my meal!"
    b "I can become friends with the cute little fairies and spirits in the Magic Town instead of making them my slaves."
    b "Oh my god, the dish is taking effect! I feel myself turning kinder, softer, almost tender. It's... surprisingly wonderful!"
    b "I have to go thank that cute spirit for his dish and tell him that I'm not going to hurt them anymore!"
    jump ending
label ending:
    scene celebrate with fade
    play music "crowd-cheer-406646.mp3"
    m "So that's how I became the hero of the Magic Town."
    m "I made this sweet place safe again."
    m "Honestly? I'm pretty proud of myself."
    play music "dawn-logo-430179.mp3"
    scene theend with fade
    pause 4.0
    return


