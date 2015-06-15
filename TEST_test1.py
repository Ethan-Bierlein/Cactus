from sys import exit
import cactus

FLOWCHART = cactus.Flowchart({
    "data": {
        "start": cactus.Position({
            "name":       "start",
            "desc_enter": "Description on enter.",
            "desc_exit":  "Description on exit.",
            "choices": {
                "choice1": "1",
                "choice2": "2"
            }
        }),
        "1": cactus.Position({
            "name":       "Name Goes Here 1",
            "desc_enter": "Description on enter.",
            "desc_exit":  "Description on exit.",
            "choices":    {}
        }),
        "2": cactus.Position({
            "name":       "Name Goes Here 2",
            "desc_enter": "Description on enter.",
            "desc_exit":  "Description on exit.",
            "choices":    {}
        })
    }
})


GAME = cactus.Game({
    "name":              "Game Name",
    "desc":              "Game Description",
    "prompt":            "> ",
    "invalid_input_msg": "Invalid input",
    "flowchart":         FLOWCHART,
    "case_sensitive":    False,
    "allow_help":        True,
    "about_text":        "Write about your game here.",
    "event_handlers": {
        "position.Name Goes Here 1.enter.after": exit,
        "position.Name Goes Here 2.enter.after": exit
    }
})


GAME.play_game()
