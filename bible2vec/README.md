# Bible2Vec
Use [Word2vec](https://en.wikipedia.org/wiki/Word2vec) to find similar scriptures. Here is a sample output:

>In the beginning God created the heaven and the earth. ~ Genesis 1:1

Scripture | Text | Score
--- | --- | ---
Genesis 2:4 | These are the generations of the heavens and of the earth when they were created, in the day that the LORD God made the earth and the heavens, | 0.86
Genesis 6:13 | And God said unto Noah, The end of all flesh is come before me; for the earth is filled with violence through them; and, behold, I will destroy them with the earth. | 0.81
1 Kings 8:27 | But will God indeed dwell on the earth? behold, the heaven and heaven of heavens cannot contain thee; how much less this house that I have builded? | 0.8
Genesis 1:17 | And God set them in the firmament of the heaven to give light upon the earth, | 0.8
John 1:2 | The same was in the beginning with God. | 0.78
Genesis 6:17 | And, behold, I, even I, do bring a flood of waters upon the earth, to destroy all flesh, wherein is the breath of life, from under heaven; and every thing that is in the earth shall die. | 0.78
Psalms 113:6 | Who humbleth himself to behold the things that are in heaven, and in the earth! | 0.78
Jeremiah 22:29 | O earth, earth, earth, hear the word of the LORD. | 0.77
Psalms 68:8 | The earth shook, the heavens also dropped at the presence of God: even Sinai itself was moved at the presence of God, the God of Israel. | 0.77
Deuteronomy 10:14 | Behold, the heaven and the heaven of heavens is the LORD's thy God, the earth also, with all that therein is. | 0.77

## Installation

```bash
python3.5 -m venv venv          # Create clean virtual environment
source venv/bin/activate        # Activate virtual environment
pip install -r requirements.txt # Install dependencies
```

This repo contains a Bible dataset (King James) but you will need to run [wiki2vec](...) to create the Word2vec model.
