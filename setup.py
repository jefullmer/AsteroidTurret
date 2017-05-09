import cx_Freeze

executables = [cx_Freeze.Executable("space_ship_game.py")]

cx_Freeze.setup(name="Asteroid Defence",
                options={"build_exe": {"packages":["pygame"],
                                       "include_files":["highscore.ahs", "sprites", "audio"]}},
                executables = executables)
