from sys import exit
import cactus

flowchart = cactus.Flowchart({
    "data": [
        cactus.Position({
            "name": "start",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {
                "choice1": 1,
                "choice2": 2
            }
        }),
        cactus.Position({
            "name": "Name Goes Here 1",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {}
        }),
        cactus.Position({
            "name": "Name Goes Here 2",
            "desc_enter": "Description on enter.",
            "desc_exit": "Description on exit.",
            "choices": {}
        })
    ]
})


game = cactus.Game({
    "name": "Game Name",
    "desc": "Game Description",
    "prompt": "> ",
    "invalid_input_msg": "Invalid input",
    "flowchart": flowchart,
    "case_sensitive": False,
    "allow_help": True,
    "about_text": "Write about your game here.",
    "event_handlers": {
        "position.name goes here 1.enter.after": exit,
        "position.name goes here 2.enter.after": exit
    }
})

game.play_game()
