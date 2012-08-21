# Copyright (c) 2012 Jonathan Topf

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# ms_export_translate() contains the definitions of the appleseed XML scene entities, it also contains the code for translating the maya object heirarchy into the appleseed object heirarchy

#****************************************************************************************************************************************************************************************************
# utilitiy functions & classes **********************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************

# OutXML *****************************************************************************************************************************************************************************************

class XMLObject():
spaces_per_indentation_level = 4    
    def __init__(self, f_path):
        self.file_path = f_path
        self.indentation_level = 0
        self.file_object = None
        try:
            self.file_object = open(self.file_path, 'w') #open file for editing

        except IOError:
            cmds.error('IO error: file not accesable')
            raise RuntimeError('IO error: file not accesable')
            return
        
    def appendLine(self, str):
        self.file_object.write(((self.indentation_level * self.spaces_per_indentation_level) * ' ') + str + '\n')
     
     def startElement(self,str):
     	self.appendLine('<' + str + '>')
        self.indentation_level += 1
        
    def endElement(self, str):
        self.indentation_level -= 1
        self.appendLine('</' + str + '>')
        
    def appendElement(self, str):
        self.appendLine('<' + str + '>')

    def appendParameter(self, name, value):
    	self.appendElement('parameter name"{0}" value="{1}"'.format(name, value))

    def close(self):
        self.file_object.close() #close file

#****************************************************************************************************************************************************************************************************
# appleseed As classes ******************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************

# AsProject *****************************************************************************************************************************************************************************************

class AsProject():
	def __init__(self, maya_scene):
		pass
	def emit_XML(file):
		pass

# AsScene *******************************************************************************************************************************************************************************************

# AsCamera ******************************************************************************************************************************************************************************************

# AsTransform ***************************************************************************************************************************************************************************************

# AsTexture *****************************************************************************************************************************************************************************************

# AsEnvironmentEdf **********************************************************************************************************************************************************************************

# AsEnvironmentShader *******************************************************************************************************************************************************************************

# AsColor *******************************************************************************************************************************************************************************************

# AsEnvironment *************************************************************************************************************************************************************************************

# AsAssembly ****************************************************************************************************************************************************************************************

# AsMaterial ****************************************************************************************************************************************************************************************

# AsObject ******************************************************************************************************************************************************************************************

# AsBsdf ********************************************************************************************************************************************************************************************

# AsEdf *********************************************************************************************************************************************************************************************

# AsSurfaceShader ***********************************************************************************************************************************************************************************

# AsOutput ******************************************************************************************************************************************************************************************

# AsConfiguration ***********************************************************************************************************************************************************************************





#****************************************************************************************************************************************************************************************************
# translate() function ******************************************************************************************************************************************************************************
#****************************************************************************************************************************************************************************************************





