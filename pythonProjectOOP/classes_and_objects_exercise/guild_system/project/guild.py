from classes_and_objects_exercise.spoopify.project import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player not in self.players:
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
            return f"Player {player.name} is in another guild."
        return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                p.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        result += "\n".join([Player.player_info(p) for p in self.players])
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())