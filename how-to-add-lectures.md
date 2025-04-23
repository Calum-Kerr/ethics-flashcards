# How to Add New Lectures to Your Ethics Study Hub

This guide explains how to add new lecture summaries and flashcards to your Ethics Study Hub.

## Adding a New Lecture Summary

1. **Create a new summary page**:
   - Make a copy of `summary-template.html`
   - Rename it to `summary-lecture2.html` (or the appropriate lecture number)
   - Edit the content to match your new lecture

2. **Update the title and header**:
   ```html
   <title>Lecture 2: TITLE HERE - Summary</title>
   ```
   ```html
   <h1>Lecture 2: TITLE HERE</h1>
   ```

3. **Add your summary content**:
   - Replace the placeholder content in the `summary-content` section
   - Use `<h2>` for main topics and `<h3>` for subtopics
   - Use `<ul>` and `<li>` for bullet points

4. **Update the summaries hub**:
   - Open `summaries.html`
   - Add a new entry to the lecture list:
   ```html
   <li class="lecture-item">
       <a href="summary-lecture2.html" class="lecture-link">Lecture 2: TITLE HERE</a>
       <p class="lecture-description">Brief description of the lecture content.</p>
   </li>
   ```

## Adding New Flashcards

1. **Open the flashcards file**:
   - Edit `ethics-flashcards.html`

2. **Find the flashcards array**:
   - Look for `const flashcards = [` (around line 200)

3. **Add new flashcard entries**:
   ```javascript
   {
       question: "Your new question here?",
       answer: "Your new answer here."
   },
   ```

4. **Save the file**:
   - Make sure to maintain the correct syntax with commas between entries

## Pushing Changes to GitHub

1. Go to your GitHub repository: https://github.com/Calum-Kerr/ethics-flashcards
2. Upload the new files or edit existing files
3. Commit your changes
4. GitHub Pages will automatically update your site

## Tips for Creating Good Summaries

- Focus on key concepts and definitions
- Use headings to organize content logically
- Keep paragraphs short and focused
- Use bullet points for lists of related items
- Include examples where helpful

## Tips for Creating Good Flashcards

- Keep questions clear and specific
- Make sure answers are concise but complete
- Focus on one concept per flashcard
- Include important definitions and relationships
- Create application questions that test understanding, not just memorization
