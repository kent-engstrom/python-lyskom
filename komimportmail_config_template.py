import kom

# -- CONFIGURATION BEGINS HERE ---

# How to connect to the server. 
KOMSERVER = "FIXME"     # Name or IP address
KOMPORT = 4894		    # Port number

# The LysKOM person that's author of the imported mails. Should
# preferably be a person with only mailimport as responsibility.
KOMPERSON = FIXME           # LysKOM person number
KOMPASSSWORD = "FIXME"      # Password of KOMPERSON

# File to log some information into. Make sure the user executing
# komimportmail has write-permissions in the directory where this file
# resides.
LOG_FILE = "/FIXME/maillog"

# File for message-id -> text-no database
# Note: the actual filename depends on what database shelve.py
# chooses.
# As for the LOG_FILE, the user running komimportmail must have
# write-permissions here too.
ID_DB_FILE = "/FIXME/message-id"

# Text to prepend to subject header of appendices
APPENDIX_SUBJECT_PREFIX_NONAME = "Bilaga till: "
APPENDIX_SUBJECT_PREFIX = "Bilaga (%s) till: "

# Use comments or footnotes when linking appendices to the main article?
APPENDIX_COMMENT_TYPE = kom.MIC_COMMENT #or kom.MIC_FOOTNOTE

# Skip AI_MX_DATE (for use with buggy aux-items.conf:s)
SKIP_AI_MX_DATE = 0

# Remove reduntant text/html after text/plain in mails with
# MIME-parts with content-type multipart/alternative.
REMOVE_REDUNDANT_HTML = 1

# -- CONFIGURATION ENDS HERE ---
