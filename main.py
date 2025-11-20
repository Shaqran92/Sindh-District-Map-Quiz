from turtle import Screen, Turtle
import pandas as pd
import os

class SindhDistrictsGame:
    def __init__(self):
        # Game settings
        self.correct = 0
        self.total_districts = 24
        self.guessed_districts = []
        self.font_main = ("Arial", 8, "bold")
        self.font_title = ("Arial", 14, "bold")
        self.font_score = ("Arial", 12, "normal")
        
        # Setup screen
        self.setup_screen()
        
        # Load data
        self.load_data()
        
        # Setup UI elements
        self.setup_ui()
        
    def setup_screen(self):
        """Initialize and configure the game screen"""
        self.screen = Screen()
        self.screen.setup(700, 700)
        self.screen.title("Sindh Districts Game - Educational Quiz")
        self.screen.bgcolor("#E8F4F8")
        
        # Check if image exists before adding
        if os.path.exists("Sindh_Districts.gif"):
            self.screen.addshape("Sindh_Districts.gif")
        else:
            print("Warning: Sindh_Districts.gif not found!")
        
        # Enable coordinate tracking (useful for development)
        self.screen.onscreenclick(self.get_mouse_click_coor)
        
    def load_data(self):
        """Load districts data from CSV file"""
        try:
            self.data = pd.read_csv("Districts.csv")
            self.districts_list = self.data.state.str.title().tolist()
            self.total_districts = len(self.districts_list)
        except FileNotFoundError:
            print("Error: Districts.csv file not found!")
            self.screen.bye()
            exit()
        except Exception as e:
            print(f"Error loading data: {e}")
            self.screen.bye()
            exit()
    
    def setup_ui(self):
        """Setup UI elements including map and score display"""
        # Map turtle
        self.map_turtle = Turtle()
        self.map_turtle.speed(0)
        if os.path.exists("Sindh_Districts.gif"):
            self.map_turtle.shape("Sindh_Districts.gif")
        else:
            # Fallback to square if image not found
            self.map_turtle.shape("square")
            self.map_turtle.shapesize(20, 20)
            self.map_turtle.color("lightgray")
        
        # Score display
        self.score_display = Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.goto(0, 320)
        self.update_score_display()
        
        # Instructions display
        self.show_instructions()
        
    def show_instructions(self):
        """Display game instructions"""
        instructions = Turtle()
        instructions.hideturtle()
        instructions.penup()
        instructions.goto(0, -320)
        instructions.write("Type 'Exit' to quit | Type 'Show' to reveal remaining districts", 
                         align="center", font=("Arial", 10, "italic"))
        
    def update_score_display(self):
        """Update the score display"""
        self.score_display.clear()
        self.score_display.write(f"Score: {self.correct}/{self.total_districts} Districts", 
                                align="center", font=self.font_title)
        
    def get_mouse_click_coor(self, x, y):
        """Print coordinates when clicking on map (for development)"""
        print(f"Coordinates: ({x:.0f}, {y:.0f})")
        
    def write_district_name(self, district_name, x, y):
        """Write district name on the map"""
        text_turtle = Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.goto(x, y)
        text_turtle.color("darkblue")
        text_turtle.write(district_name, align="center", font=self.font_main)
        
    def show_remaining_districts(self):
        """Display all remaining districts in red"""
        remaining = set(self.districts_list) - set(self.guessed_districts)
        
        for district in remaining:
            district_data = self.data[self.data.state.str.title() == district]
            if not district_data.empty:
                x = district_data.x.iloc[0]
                y = district_data.y.iloc[0]
                
                # Write in red to show it was missed
                text_turtle = Turtle()
                text_turtle.hideturtle()
                text_turtle.penup()
                text_turtle.goto(x, y)
                text_turtle.color("red")
                text_turtle.write(district, align="center", font=self.font_main)
        
        # Show completion message
        self.show_game_over_message(show_missed=True)
        
    def show_game_over_message(self, show_missed=False):
        """Display game over message"""
        message_turtle = Turtle()
        message_turtle.hideturtle()
        message_turtle.penup()
        message_turtle.goto(0, 0)
        
        if self.correct == self.total_districts:
            message_turtle.color("green")
            message_turtle.write("🎉 Congratulations! You got all districts! 🎉", 
                               align="center", font=("Arial", 20, "bold"))
        elif show_missed:
            message_turtle.goto(0, -280)
            message_turtle.color("orange")
            message_turtle.write(f"Game Over! You found {self.correct}/{self.total_districts} districts. Red ones were missed.", 
                               align="center", font=("Arial", 12, "bold"))
            
    def play(self):
        """Main game loop"""
        while self.correct < self.total_districts:
            # Get user input
            answer = self.screen.textinput(
                title=f"{self.correct}/{self.total_districts} Districts Correct",
                prompt="Enter a district name (or 'Exit' to quit, 'Show' to reveal all):"
            )
            
            # Handle empty input
            if answer is None or answer.strip() == "":
                continue
                
            answer = answer.strip().title()
            
            # Check for special commands
            if answer.lower() == "exit":
                self.show_remaining_districts()
                break
            elif answer.lower() == "show":
                self.show_remaining_districts()
                break
            
            # Check if district exists and hasn't been guessed
            if answer in self.districts_list:
                if answer not in self.guessed_districts:
                    # Get coordinates
                    district_data = self.data[self.data.state.str.title() == answer]
                    if not district_data.empty:
                        x = district_data.x.iloc[0]
                        y = district_data.y.iloc[0]
                        
                        # Write district name on map
                        self.write_district_name(answer, x, y)
                        
                        # Update game state
                        self.guessed_districts.append(answer)
                        self.correct += 1
                        self.update_score_display()
                        
                        # Check for win condition
                        if self.correct == self.total_districts:
                            self.show_game_over_message()
                            break
                else:
                    # Already guessed
                    self.show_message("Already Guessed!", "orange")
            else:
                # Wrong answer
                self.show_message("Not a valid district!", "red")
                
    def show_message(self, text, color):
        """Show temporary message to user"""
        msg_turtle = Turtle()
        msg_turtle.hideturtle()
        msg_turtle.penup()
        msg_turtle.goto(0, -260)
        msg_turtle.color(color)
        msg_turtle.write(text, align="center", font=("Arial", 11, "italic"))
        self.screen.ontimer(lambda: msg_turtle.clear(), 2000)  # Clear after 2 seconds
        
    def run(self):
        """Start the game"""
        self.play()
        self.screen.exitonclick()

# Run the game
if __name__ == "__main__":
    game = SindhDistrictsGame()
    game.run()