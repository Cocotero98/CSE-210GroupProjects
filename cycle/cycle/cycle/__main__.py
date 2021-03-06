<<<<<<< HEAD

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.casting.player2 import Player2
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.scripting.grow import Grow
from game.casting.score2 import Score2

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("snakes", Snake())
    cast.add_actor("scores", Score())
    cast.add_actor("player2", Player2())
    cast.add_actor('score2', Score2())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("update", Grow())
    
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
=======
import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.scripting.grow import Grow

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("snakes", Snake(int(constants.MAX_X / 4),int(constants.MAX_Y / 2)))
    cast.add_actor("scores", Score(Point(0, 0),'one'))
    cast.add_actor("player2", Snake(int(constants.MAX_X / 2)+int(constants.MAX_X / 4),int(constants.MAX_Y / 2)))
    cast.add_actor('score2', Score(Point(780, 0),'two'))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("update", Grow())
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
>>>>>>> 29c236b51c6c9b19ce3bbb1131125b811b8855ad
    main()