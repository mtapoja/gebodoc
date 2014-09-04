gebodoc
=======

Information collector and document creator

gebodoc collects information from various sources (such as data files,
Excel docs, database, Jira, Bugzilla, version control etc.) and create documents
out of it. Resulting document formats can be for example HTML, text or PDF, and
it basically depends on the used template format and used document build command.

If you combine data sources, templates, gebodoc and scheduled runs, you get
automated document generation.

Example uses where gebodoc should help:
- create several CVs to same template and produce PDF.
- create recurring release notes with release status data (fixed bugs, new features
  free form data).
- status reports of any kind, automatically! Yay!
- error management report (bug statuses and changes between releases).

Implemented features:
- data file reading and processing
- textual template processing (Cheetah templates)
- Ubuntu PPA for easy deployment and updates (sudo apt-add-repository ppa:mtapoja/tools)
- Example for creating a CV for Donald Duck.

Planned features include (but probably are not limited to):
- data sources:
  * local textual data (e.g. csv or plain text)
  * textual data from URL
  * bug/issue systems (Jira, Bugzilla)
  * version control (git), also repo manifest (XML format used by Googlen repo tool)
  * Excel file
  * LibreOffice Calc file
  * several configuration and data formats (e.g. INI forma, probably YAML, JSON, XML)
  * SQLite database (maybe from actual database servers too)

Where's the name comes from?
See: http://runesecrets.com/rune-meanings/gebo
