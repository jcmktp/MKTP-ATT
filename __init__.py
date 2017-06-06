# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BufferForm
                                 A QGIS plugin
 test to generate bufferq
                             -------------------
        begin                : 2017-06-05
        copyright            : (C) 2017 by Julio Canas 
        email                : jc609a@att.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BufferForm class from file BufferForm.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Buffer_Form import BufferForm
    return BufferForm(iface)
