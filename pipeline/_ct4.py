# ./_ct4.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9d1f6fbb0700f1fbe55a4d27e34bb49011ad1e27
# Generated 2026-02-02 18:03:54.409433 by PyXB version 1.2.6 using Python 3.14.0.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v4 [xmlns:ct4]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c741fc79-0a5d-4071-ac2f-90019036e17c')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v4', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v4}ToiletType
class ToiletType (pyxb.binding.datatypes.string):

    """An indication of the availability of a toilet in a coach in a train formation. E.g. "Unknown", "None" , "Standard" or "Accessible". Note that other values may be supplied in the future without a schema change."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ToiletType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v4.xsd', 13, 1)
    _Documentation = 'An indication of the availability of a toilet in a coach in a train formation. E.g. "Unknown", "None" , "Standard" or "Accessible". Note that other values may be supplied in the future without a schema change.'
ToiletType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ToiletType', ToiletType)
_module_typeBindings.ToiletType = ToiletType

# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v4}ToiletStatus
class ToiletStatus (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """The service status of a toilet in coach formation data."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ToiletStatus')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v4.xsd', 19, 1)
    _Documentation = 'The service status of a toilet in coach formation data.'
ToiletStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=ToiletStatus)
ToiletStatus.Unknown = ToiletStatus._CF_enumeration.addEnumeration(unicode_value='Unknown', tag='Unknown')
ToiletStatus.InService = ToiletStatus._CF_enumeration.addEnumeration(unicode_value='InService', tag='InService')
ToiletStatus.NotInService = ToiletStatus._CF_enumeration.addEnumeration(unicode_value='NotInService', tag='NotInService')
ToiletStatus._InitializeFacetMap(ToiletStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ToiletStatus', ToiletStatus)
_module_typeBindings.ToiletStatus = ToiletStatus

# Complex type {http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v4}ToiletAvailabilityType with content type SIMPLE
class ToiletAvailabilityType (pyxb.binding.basis.complexTypeDefinition):
    """The availability of a toilet in coach formation data. If no availability is supplied, it should be assumed to have the value "Unknown"."""
    _TypeDefinition = ToiletType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ToiletAvailabilityType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v4.xsd', 30, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is ToiletType
    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpwww_thalesgroup_comrttiPushPortCommonTypesv4_ToiletAvailabilityType_status', _module_typeBindings.ToiletStatus, unicode_default='InService')
    __status._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v4.xsd', 36, 4)
    __status._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v4.xsd', 36, 4)
    
    status = property(__status.value, __status.set, None, 'The service status of this toilet. E.g. "Unknown", "InService" or "NotInService".')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __status.name() : __status
    })
_module_typeBindings.ToiletAvailabilityType = ToiletAvailabilityType
Namespace.addCategoryObject('typeBinding', 'ToiletAvailabilityType', ToiletAvailabilityType)

