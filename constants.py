CLIENT_ID = "dd2485fee3014d9395070ebc54d45429"
CLIENT_SECRET = "563528512f4f4a5f930b4844d61550db"
API_ID = 1473170
API_HASH = "13b5f343df92127984570f036182ad11"
INITIAL_TOKEN = "AQAulZhGKkoNacBdf5L5GMyz57f3jYBde3YbcDr2QOVtYtIBVMx8V9HNx0Edg-IU8t39WjokDe3cQWvJ6l05upxbRShHb0ezX3DnrjJDhtUz_3jHQKiJ7_ZPg5m5KM7JooLN7cJg5G2vJDNqAi3PMcEB23RKwLVqURek0vf9KTrNUiN4QrEWSJqFjuABawPXtER7lTt1ydLjmKaAXRa4ZG-TO0pUFlu4N_8ctIfdoxlH_SROvTlO"
INITIAL_BIO = "FLY ON THE WALL"
LOG = "me"
# the escaping is necessary since we are testing against a regex pattern with it.
SHUTDOWN_COMMAND = "\/\/stop"
# The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
# NEVER use whatever you put here in your original bio. NEVER. Don't do it!
KEY = '🎶'
# The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
BIOS = [KEY + ' Now Playing: {interpret} - {title} {progress}/{duration}',
        KEY + ' Now Playing: {interpret} - {title}',
        KEY + ' : {interpret} - {title}',
        KEY + ' Now Playing: {title}',
        KEY + ' : {title}']
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
