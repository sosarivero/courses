str = 'X-DSPAM-Confidence:0.8475'

# Use find to get position of the colon
colonpos = str.find(':')
# Slice and strip of whitespace  to get the number
confidencevalue = str[colonpos + 1:].strip()
# Convert to float
confidencefloat = float(confidencevalue)
# Print it for test check
print(confidencefloat)
