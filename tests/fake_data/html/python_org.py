# https://docs.python.org/3/
source = """<html xmlns="http://www.w3.org/1999/xhtml"><head>
    <meta charset="utf-8"><title>3.7.4 Documentation</title>
    <link rel="stylesheet" href="_static/pydoctheme.css" type="text/css">
    <link rel="stylesheet" href="_static/pygments.css" type="text/css">
    
    <script type="text/javascript" id="documentation_options" data-url_root="./" src="_static/documentation_options.js"></script>
    <script type="text/javascript" src="_static/jquery.js"></script>
    <script type="text/javascript" src="_static/underscore.js"></script>
    <script type="text/javascript" src="_static/doctools.js"></script>
    <script type="text/javascript" src="_static/language_data.js"></script>
    
    <script type="text/javascript" src="_static/sidebar.js"></script>
    
    <link rel="search" type="application/opensearchdescription+xml" title="Search within Python 3.7.4 documentation" href="_static/opensearch.xml">
    <link rel="author" title="About these documents" href="about.html">
    <link rel="index" title="Index" href="genindex.html">
    <link rel="search" title="Search" href="search.html">
    <link rel="copyright" title="Copyright" href="copyright.html">
    <link rel="shortcut icon" type="image/png" href="_static/py.png">
    <link rel="canonical" href="https://docs.python.org/3/index.html">
    
    <script type="text/javascript" src="_static/copybutton.js"></script>
    <script type="text/javascript" src="_static/switchers.js"></script>
    
    
    
    <style>
      @media only screen {
        table.full-width-table {
            width: 100%;
        }
      }
    </style>
 

  </head><body>
  
    <div class="related" role="navigation" aria-label="related navigation" style="user-select: auto;">
      <h3 style="user-select: auto;">Navigation</h3>
      <ul style="user-select: auto;">
        <li class="right" style="margin-right: 10px; user-select: auto;">
          <a href="genindex.html" title="General Index" accesskey="I" style="user-select: auto;">index</a></li>
        <li class="right" style="user-select: auto;">
          <a href="py-modindex.html" title="Python Module Index" style="user-select: auto;">modules</a> |</li>
        <li style="user-select: auto;"><img src="_static/py.png" alt="" style="vertical-align: middle; margin-top: -1px; user-select: auto;"></li>
        <li style="user-select: auto;"><a href="https://www.python.org/" style="user-select: auto;">Python</a> »</li>
        <li style="user-select: auto;">
          <span class="language_switcher_placeholder" style="user-select: auto;"><select><option value="en" selected="selected">English</option><option value="fr">French</option><option value="ja">Japanese</option><option value="ko">Korean</option><option value="zh-cn">Simplified Chinese</option></select></span>
          <span class="version_switcher_placeholder" style="user-select: auto;"><select><option value="3.9">dev (3.9)</option><option value="3.8">pre (3.8)</option><option value="3.7" selected="selected">3.7.4</option><option value="3.6">3.6</option><option value="3.5">3.5</option><option value="2.7">2.7</option></select></span>
          <a href="#" style="user-select: auto;">Documentation </a> »
        </li>

    <li class="right" style="user-select: auto;">
        

    <div class="inline-search" style="user-select: auto;" role="search">
        <form class="inline-search" action="search.html" method="get" style="user-select: auto;">
          <input placeholder="Quick search" type="text" name="q" style="user-select: auto;">
          <input type="submit" value="Go" style="user-select: auto;">
          <input type="hidden" name="check_keywords" value="yes" style="user-select: auto;">
          <input type="hidden" name="area" value="default" style="user-select: auto;">
        </form>
    </div>
    <script type="text/javascript" style="user-select: auto;">$('.inline-search').show(0);</script>
         |
    </li>

      </ul>
    </div>    

    <div class="document" style="user-select: auto;">
      <div class="documentwrapper" style="user-select: auto;">
        <div class="bodywrapper" style="user-select: auto;">
          <div class="body" role="main" style="user-select: auto;">
            
  <h1 style="user-select: auto;">Python 3.7.4 documentation</h1>
  <p style="user-select: auto;">
  Welcome! This is the documentation for Python 3.7.4.
  </p>
  <p style="user-select: auto;"><strong style="user-select: auto;">Parts of the documentation:</strong></p>
  <table class="contentstable" align="center" style="user-select: auto;"><tbody style="user-select: auto;"><tr style="user-select: auto;">
    <td width="50%" style="user-select: auto;">
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="whatsnew/3.7.html" style="user-select: auto;">What's new in Python 3.7?</a><br style="user-select: auto;">
        <span class="linkdescr" style="user-select: auto;"> or <a href="whatsnew/index.html" style="user-select: auto;">all "What's new" documents</a> since 2.0</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="tutorial/index.html" style="user-select: auto;">Tutorial</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">start here</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="library/index.html" style="user-select: auto;">Library Reference</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">keep this under your pillow</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="reference/index.html" style="user-select: auto;">Language Reference</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">describes syntax and language elements</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="using/index.html" style="user-select: auto;">Python Setup and Usage</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">how to use Python on different platforms</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="howto/index.html" style="user-select: auto;">Python HOWTOs</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">in-depth documents on specific topics</span></p>
    </td><td width="50%" style="user-select: auto;">
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="installing/index.html" style="user-select: auto;">Installing Python Modules</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">installing from the Python Package Index &amp; other sources</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="distributing/index.html" style="user-select: auto;">Distributing Python Modules</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">publishing modules for installation by others</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="extending/index.html" style="user-select: auto;">Extending and Embedding</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">tutorial for C/C++ programmers</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="c-api/index.html" style="user-select: auto;">Python/C API</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">reference for C/C++ programmers</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="faq/index.html" style="user-select: auto;">FAQs</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">frequently asked questions (with answers!)</span></p>
    </td></tr>
  </tbody></table>

  <p style="user-select: auto;"><strong style="user-select: auto;">Indices and tables:</strong></p>
  <table class="contentstable" align="center" style="user-select: auto;"><tbody style="user-select: auto;"><tr style="user-select: auto;">
    <td width="50%" style="user-select: auto;">
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="py-modindex.html" style="user-select: auto;">Global Module Index</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">quick access to all modules</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="genindex.html" style="user-select: auto;">General Index</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">all functions, classes, terms</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="glossary.html" style="user-select: auto;">Glossary</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">the most important terms explained</span></p>
    </td><td width="50%" style="user-select: auto;">
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="search.html" style="user-select: auto;">Search page</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">search this documentation</span></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="contents.html" style="user-select: auto;">Complete Table of Contents</a><br style="user-select: auto;">
         <span class="linkdescr" style="user-select: auto;">lists all sections and subsections</span></p>
    </td></tr>
  </tbody></table>

  <p style="user-select: auto;"><strong style="user-select: auto;">Meta information:</strong></p>
  <table class="contentstable" align="center" style="user-select: auto;"><tbody style="user-select: auto;"><tr style="user-select: auto;">
    <td width="50%" style="user-select: auto;">
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="bugs.html" style="user-select: auto;">Reporting bugs</a></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="about.html" style="user-select: auto;">About the documentation</a></p>
    </td><td width="50%" style="user-select: auto;">
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="license.html" style="user-select: auto;">History and License of Python</a></p>
      <p class="biglink" style="user-select: auto;"><a class="biglink" href="copyright.html" style="user-select: auto;">Copyright</a></p>
    </td></tr>
  </tbody></table>

          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation" style="user-select: auto;">
        <div class="sphinxsidebarwrapper" style="user-select: auto; float: left; margin-right: 0px; width: 202px;"><h3 style="user-select: auto;">Download</h3>
<p style="user-select: auto;"><a href="download.html" style="user-select: auto;">Download these documents</a></p>
<h3 style="user-select: auto;">Docs by version</h3>
<ul style="user-select: auto;">
  <li style="user-select: auto;"><a href="https://docs.python.org/3.9/" style="user-select: auto;">Python 3.9 (in development)</a></li>
  <li style="user-select: auto;"><a href="https://docs.python.org/3.8/" style="user-select: auto;">Python 3.8 (pre-release)</a></li>
  <li style="user-select: auto;"><a href="https://docs.python.org/3.7/" style="user-select: auto;">Python 3.7 (stable)</a></li>
  <li style="user-select: auto;"><a href="https://docs.python.org/3.6/" style="user-select: auto;">Python 3.6 (security-fixes)</a></li>
  <li style="user-select: auto;"><a href="https://docs.python.org/3.5/" style="user-select: auto;">Python 3.5 (security-fixes)</a></li>
  <li style="user-select: auto;"><a href="https://docs.python.org/2.7/" style="user-select: auto;">Python 2.7 (stable)</a></li>
  <li style="user-select: auto;"><a href="https://www.python.org/doc/versions/" style="user-select: auto;">All versions</a></li>
</ul>

<h3 style="user-select: auto;">Other resources</h3>
<ul style="user-select: auto;">
  
  <li style="user-select: auto;"><a href="https://www.python.org/dev/peps/" style="user-select: auto;">PEP Index</a></li>
  <li style="user-select: auto;"><a href="https://wiki.python.org/moin/BeginnersGuide" style="user-select: auto;">Beginner's Guide</a></li>
  <li style="user-select: auto;"><a href="https://wiki.python.org/moin/PythonBooks" style="user-select: auto;">Book List</a></li>
  <li style="user-select: auto;"><a href="https://www.python.org/doc/av/" style="user-select: auto;">Audio/Visual Talks</a></li>
</ul>
        </div>
      <div id="sidebarbutton" title="Collapse sidebar" style="border-radius: 0px 5px 5px 0px; color: rgb(68, 68, 68); background-color: rgb(204, 204, 204); font-size: 1.2em; cursor: pointer; height: 914.188px; padding-top: 1px; padding-left: 1px; margin-left: 218px;"><span style="display: block; position: fixed; top: 399.5px;">«</span></div></div>
      <div class="clearer" style="user-select: auto;"></div>
    </div>  
    <div class="related" role="navigation" aria-label="related navigation" style="user-select: auto;">
      <h3 style="user-select: auto;">Navigation</h3>
      <ul style="user-select: auto;">
        <li class="right" style="margin-right: 10px; user-select: auto;">
          <a href="genindex.html" title="General Index" style="user-select: auto;">index</a></li>
        <li class="right" style="user-select: auto;">
          <a href="py-modindex.html" title="Python Module Index" style="user-select: auto;">modules</a> |</li>
        <li style="user-select: auto;"><img src="_static/py.png" alt="" style="vertical-align: middle; margin-top: -1px; user-select: auto;"></li>
        <li style="user-select: auto;"><a href="https://www.python.org/" style="user-select: auto;">Python</a> »</li>
        <li style="user-select: auto;">
          <span class="language_switcher_placeholder" style="user-select: auto;"><select><option value="en" selected="selected">English</option><option value="fr">French</option><option value="ja">Japanese</option><option value="ko">Korean</option><option value="zh-cn">Simplified Chinese</option></select></span>
          <span class="version_switcher_placeholder" style="user-select: auto;"><select><option value="3.9">dev (3.9)</option><option value="3.8">pre (3.8)</option><option value="3.7" selected="selected">3.7.4</option><option value="3.6">3.6</option><option value="3.5">3.5</option><option value="2.7">2.7</option></select></span>
          <a href="#" style="user-select: auto;">Documentation </a> »
        </li>

    <li class="right" style="user-select: auto;">
        

    <div class="inline-search" style="user-select: auto;" role="search">
        <form class="inline-search" action="search.html" method="get" style="user-select: auto;">
          <input placeholder="Quick search" type="text" name="q" style="user-select: auto;">
          <input type="submit" value="Go" style="user-select: auto;">
          <input type="hidden" name="check_keywords" value="yes" style="user-select: auto;">
          <input type="hidden" name="area" value="default" style="user-select: auto;">
        </form>
    </div>
    <script type="text/javascript" style="user-select: auto;">$('.inline-search').show(0);</script>
         |
    </li>

      </ul>
    </div>  
    <div class="footer" style="user-select: auto;">
    © <a href="copyright.html" style="user-select: auto;">Copyright</a> 2001-2019, Python Software Foundation.
    <br style="user-select: auto;">
    The Python Software Foundation is a non-profit corporation.
    <a href="https://www.python.org/psf/donations/" style="user-select: auto;">Please donate.</a>
    <br style="user-select: auto;">
    Last updated on Sep 07, 2019.
    <a href="bugs.html" style="user-select: auto;">Found a bug</a>?
    <br style="user-select: auto;">
    Created using <a href="http://sphinx.pocoo.org/" style="user-select: auto;">Sphinx</a> 2.0.1.
    </div>

  
<div class="liner-mini-button" style="display: none;"><a class="liner-mb liner-save-button" style="background-image: url('chrome-extension://ooelpmkcpjkmoffkdgefbejfgfpafhic/images/mini-btn@3x.png') !important;"></a></div><div class="liner-mini-tooltip" style="display: none;"><span class="liner-color-yellow liner-mini-color-circle liner-save-button"></span><span class="liner-color-green liner-mini-color-circle liner-save-button"></span><span class="liner-color-orange liner-mini-color-circle liner-save-button"></span><span class="liner-color-violet liner-mini-color-circle liner-save-button"></span><span class="liner-color-blue liner-mini-color-circle liner-save-button"></span><span class="liner-color-pink liner-mini-color-circle liner-save-button"></span></div><div class="liner-tooltip-wrap"><div class="liner-tooltip-menu"><span class="liner-tooltip-color liner-tooltip-icon"></span><span class="liner-tooltip-comment liner-tooltip-icon"></span><span class="liner-tooltip-undo liner-tooltip-icon"></span></div><div class="liner-color-picker"><span class="liner-color-yellow liner-color-circle"></span><span class="liner-color-green liner-color-circle"></span><span class="liner-color-orange liner-color-circle"></span><span class="liner-color-violet liner-color-circle"></span><span class="liner-color-blue liner-color-circle"></span><span class="liner-color-pink liner-color-circle"></span></div><div class="liner-tooltip-arrow"><span class="liner-arrow-down"></span></div></div><div class="liner-comment-box"><div class="liner-comment-line"></div><div class="liner-comment-area"><textarea class="liner-comment-input" placeholder="코멘트를 작성하세요"></textarea></div></div></body><whale-quicksearch translate="no"></whale-quicksearch></html>"""