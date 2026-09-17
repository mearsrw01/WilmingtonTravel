# Legacy Capstone Assessment

## Baseline

The original May 2024 project is a three-page static website built with HTML and CSS. It demonstrates initial layout work, navigation, forms, responsive metadata and reusable styling. The submission is preserved unchanged in `legacy/` as evidence of the project's starting point.

## Findings

- Search, booking, login, registration and contact controls had no application behavior.
- There was no JavaScript, server, database or API.
- HTML contained malformed link elements, extra closing tags and inconsistent form markup.
- The interface relied on floats and fixed spacing, limiting responsive behavior.
- Some CSS selectors did not match the HTML classes they were intended to style.
- Font Awesome was loaded twice and several icon class names were obsolete.
- Image formats did not consistently match their filename extensions.
- The supplied archive did not include image licensing records.
- The project had no automated tests, dependency or deployment configuration.
- The report mentioned high-load testing, but the archive contained no scripts or results supporting that statement.

## Modernization decision

The original remains unchanged. The modern application is implemented alongside it so the repository shows a traceable improvement in architecture, accessibility, validation, testing and documentation without rewriting the historical submission.
