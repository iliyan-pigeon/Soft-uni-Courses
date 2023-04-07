class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []

        for player in players:
            if player.name not in [p.name for p in self.players]:
                added_players.append(player)
                self.players.append(player)

        return f"Successfully added: {', '.join([p.name for p in added_players])}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = [p for p in self.players if p.name == player_name]

        if player:
            player = player[0]
            if player.need_sustenance is None:
                return f"{player_name} have enough stamina."

            if sustenance_type == "Food":
                if "Food" not in [s.__class__.__name__ for s in self.supplies]:
                    raise Exception("There are no food supplies left!")

                for supply in self.supplies[::-1]:
                    if supply.__class__.__name__ == "Food":
                        if player.stamina + supply.energy > 100:
                            player.stamina = 100
                        else:
                            player.stamina += supply.energy

                        self.supplies.remove(supply)
                        self.supplies = self.supplies[::-1]
                        return f"{player_name} sustained successfully with {supply.name}."

            if sustenance_type == "Drink":
                if "Drink" not in [s.__class__.__name__ for s in self.supplies]:
                    raise Exception("There are no drink supplies left!")

                for supply in self.supplies[::-1]:
                    if supply.__class__.__name__ == "Drink":
                        if player.stamina + supply.energy > 100:
                            player.stamina = 100
                        else:
                            player.stamina += supply.energy

                        self.supplies.remove(supply)
                        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player: str, second_player: str):
        not_enough_stamina_message = []
        not_enough_stamina = False

        first_player = [p for p in self.players if p.name == first_player][0]
        second_player = [p for p in self.players if p.name == second_player][0]

        if first_player.stamina == 0:
            not_enough_stamina = True
            not_enough_stamina_message.append(f"Player {first_player.name} does not have enough stamina.")
        if second_player.stamina == 0:
            not_enough_stamina = True
            not_enough_stamina_message.append(f"Player {second_player.name} does not have enough stamina.")

        if not_enough_stamina:
            return '\n'.join(not_enough_stamina_message)

        if first_player.stamina < second_player.stamina:
            if second_player.stamina - (first_player.stamina / 2) < 0:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"
            second_player.stamina -= (first_player.stamina / 2)

            if first_player.stamina - (second_player.stamina / 2) < 0:
                first_player.stamina = 0
                return f"Winner: {second_player.name}"
            first_player.stamina -= (second_player.stamina / 2)

        elif second_player.stamina < first_player.stamina:
            if first_player.stamina - (second_player.stamina / 2) < 0:
                first_player.stamina = 0
                return f"Winner: {second_player.name}"
            first_player.stamina -= (second_player.stamina / 2)

            if second_player.stamina - (first_player.stamina / 2) < 0:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"
            second_player.stamina -= (first_player.stamina / 2)

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        elif second_player.stamina > first_player.stamina:
            return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []

        for player in self.players:
            result.append(f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}")

        for supply in self.supplies:
            result.append(f"{supply.__class__.__name__}: {supply.name}, {supply.energy}")

        return '\n'.join(result)
