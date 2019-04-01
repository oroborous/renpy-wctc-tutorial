define a = Character("Alice", color="#9932CC")
define j = Character("Jane", color="#FF6347")

label start:

    play music "city outdoors.mp3"

    scene bg wctc exterior with fade

    show jane happy at left with moveinleft

    j "Oh hi! I didn't know you'd be here today."

    show alice happy at right with moveinright

    a "Hey everyone! Isn't this great? I can't wait to learn about programming."

    j "How about you? Are you excited too?"

    menu:
        "I don't know...":

            jump dislike

        "Super excited!":

            jump like

label dislike:

    "I don't know. I'm not sure if I'm going to like programming."

    show alice sad

    show jane sad

    j "Aww, don't worry. We'll help you."

    a "We can all work on our visual novel together!"

    jump computerlab

label like:

    "This is going to be so much fun!"

    show jane excited

    j "I can't wait! I have so many ideas for visual novels."

    show alice laughing

    a "Me too! Let's go inside and get started."

    jump computerlab

label computerlab:

    scene bg computer lab with fade

    play music "school.mp3"

    show jane happy at left

    show alice happy at right

    play sound "typing.mp3"

    j "Done! I can't wait to show my mom tonight."

    show jane angry

    j "I just wish we could keep working."

    show jane happy

    show alice question

    a "Hey, do you guys want to start writing a visual novel of our own?"

    menu:
        "That sounds amazing!":

            jump theend

        "I already have a ton of ideas.":

            jump theend

label theend:

    show alice laughing

    show jane excited

    j "Let's get started tomorrow!"

    "The End"

    return
