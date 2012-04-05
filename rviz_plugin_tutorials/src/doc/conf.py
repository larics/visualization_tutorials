import sys, os

sys.path += [ os.path.abspath( '.' )]

extensions = [ 'sphinx.ext.extlinks',
               'tutorialformatter' ]

# The master toctree document.
master_doc = 'index'

# The suffix of source filenames.
source_suffix = '.rst'

project = u'rviz_plugin_tutorials'

copyright = u'2012,  Willow Garage, Inc'

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

extlinks = {'svndir': ('https://code.ros.org/svn/ros-pkg/stacks/visualization_tutorials/branches/visualization_tutorials-0.6/rviz_plugin_tutorials/%s', '')}
