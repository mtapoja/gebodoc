gebodoc
=======

An information collector and document creator.

gebodoc collects information from various sources (such as data files,
Excel docs, database, Jira, Bugzilla, version control etc.) and creates documents
out of it. Resulting document formats can be for example HTML, text or PDF, and
it basically depends on the used template format and used document build command.

If you combine data sources, templates, gebodoc and scheduled runs, you get
automated document generation.

Example uses where gebodoc should help:
- Create several CVs with same template and produce PDFs.
- Create recurring release notes with release status data (fixed bugs, new features
  free form data etc.).
- Create status reports of any kind, automatically! Yay!
- Create error management report (bug statuses and changes between releases).

Implemented features:
- Data file reading and processing.
- Textual template processing (Cheetah templates).
- Ubuntu PPA for easy deployment and updates (sudo apt-add-repository ppa:mtapoja/tools).
- Example for creating a CV for Donald Duck.

Planned features include (but probably are not limited to):
- data sources:
  * local textual data (e.g. csv or ~~plain text~~)
  * textual data from URL
  * bug/issue systems (Jira, Bugzilla)
  * version control (git), also repo manifest (XML format used by Googlen repo tool)
  * Excel files
  * LibreOffice Calc files
  * several configuration and data formats (e.g. INI format, probably YAML, JSON and XML)
  * SQLite database (maybe from actual database servers too)
- template formats:
  * text format (basically any text format, such as ~~text~~ and HTML)
  * LaTeX
- output formats:
  * ~~text format~~ (basically the same than the textual template format - no conversion)
  * PDF (e.g. LaTeX to PDF)
  * HTML (e.g. LaTeX to HTML)

Where does the name comes from? See: http://runesecrets.com/rune-meanings/gebo
