class Artist:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)

    def print_info(self):
        if self.death_year == -1:
            print('Artist: {}, born {}'.format(self.name, self.birth_year))
        else:
            print('Artist: {} ({}-{})'.format(self.name, self.birth_year, self.death_year))