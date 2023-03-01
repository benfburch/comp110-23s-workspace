"""testing chat gpt wordle program."""

import wordcloud
from wordcloud import WordCloud

# Input text data as a string
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vestibulum gravida eros sit amet cursus. Sed sagittis dapibus diam eu molestie. Fusce interdum metus id massa dapibus congue. Nulla facilisi."

# Generate a wordcloud image
wordcloud = WordCloud(width = 800, height = 800, background_color ='white').generate(text)

# Display the generated image
import matplotlib.pyplot as plt
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
plt.show()