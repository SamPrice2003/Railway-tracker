# ./PPv16.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:60b06b69cd6d1987825d9d308d5a79b70e327b7a
# Generated 2026-02-02 18:03:54.409870 by PyXB version 1.2.6 using Python 3.14.0.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/v16

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
import _alm as _ImportedBinding__alm
import _ct as _ImportedBinding__ct
import _fm as _ImportedBinding__fm
import _fm2 as _ImportedBinding__fm2
import _for as _ImportedBinding__for
import _sch2 as _ImportedBinding__sch2
import _sch3 as _ImportedBinding__sch3
import _sm as _ImportedBinding__sm
import _status as _ImportedBinding__status
import _ta as _ImportedBinding__ta
import _td as _ImportedBinding__td
import _tor as _ImportedBinding__tor
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/v16', create_if_missing=True)
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


# Complex type {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse with content type ELEMENT_ONLY
class DataResponse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataResponse')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 39, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}schedule uses Python identifier schedule
    __schedule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'schedule'), 'schedule', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16schedule', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 41, 3), )

    
    schedule = property(__schedule.value, __schedule.set, None, 'Train Schedule')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}deactivated uses Python identifier deactivated
    __deactivated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'deactivated'), 'deactivated', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16deactivated', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 46, 3), )

    
    deactivated = property(__deactivated.value, __deactivated.set, None, 'Notification that a Train Schedule is now deactivated in Darwin.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}association uses Python identifier association
    __association = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'association'), 'association', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16association', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 51, 3), )

    
    association = property(__association.value, __association.set, None, 'Association between schedules')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}scheduleFormations uses Python identifier scheduleFormations
    __scheduleFormations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleFormations'), 'scheduleFormations', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16scheduleFormations', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 56, 3), )

    
    scheduleFormations = property(__scheduleFormations.value, __scheduleFormations.set, None, 'Train Formation')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}TS uses Python identifier TS
    __TS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TS'), 'TS', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16TS', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 61, 3), )

    
    TS = property(__TS.value, __TS.set, None, 'Train Status')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}formationLoading uses Python identifier formationLoading
    __formationLoading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'formationLoading'), 'formationLoading', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16formationLoading', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 66, 3), )

    
    formationLoading = property(__formationLoading.value, __formationLoading.set, None, 'Train Loading')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}OW uses Python identifier OW
    __OW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OW'), 'OW', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16OW', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 71, 3), )

    
    OW = property(__OW.value, __OW.set, None, 'Darwin Workstation Station Message')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}trainAlert uses Python identifier trainAlert
    __trainAlert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trainAlert'), 'trainAlert', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16trainAlert', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 76, 3), )

    
    trainAlert = property(__trainAlert.value, __trainAlert.set, None, 'Train Alert')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}trainOrder uses Python identifier trainOrder
    __trainOrder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trainOrder'), 'trainOrder', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16trainOrder', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 81, 3), )

    
    trainOrder = property(__trainOrder.value, __trainOrder.set, None, 'The order that trains are expected to call/pass a particular station platform')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}trackingID uses Python identifier trackingID
    __trackingID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trackingID'), 'trackingID', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16trackingID', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 86, 3), )

    
    trackingID = property(__trackingID.value, __trackingID.set, None, 'Indicate a corrected Tracking ID (headcode) for a service in a TD berth.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}alarm uses Python identifier alarm
    __alarm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'alarm'), 'alarm', '__httpwww_thalesgroup_comrttiPushPortv16_DataResponse_httpwww_thalesgroup_comrttiPushPortv16alarm', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 91, 3), )

    
    alarm = property(__alarm.value, __alarm.set, None, 'A Darwin alarm')

    _ElementMap.update({
        __schedule.name() : __schedule,
        __deactivated.name() : __deactivated,
        __association.name() : __association,
        __scheduleFormations.name() : __scheduleFormations,
        __TS.name() : __TS,
        __formationLoading.name() : __formationLoading,
        __OW.name() : __OW,
        __trainAlert.name() : __trainAlert,
        __trainOrder.name() : __trainOrder,
        __trackingID.name() : __trackingID,
        __alarm.name() : __alarm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.DataResponse = DataResponse
Namespace.addCategoryObject('typeBinding', 'DataResponse', DataResponse)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Request a standard snapshot of current database"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 127, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute viaftp uses Python identifier viaftp
    __viaftp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'viaftp'), 'viaftp', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_viaftp', pyxb.binding.datatypes.boolean, unicode_default='false')
    __viaftp._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 128, 6)
    __viaftp._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 128, 6)
    
    viaftp = property(__viaftp.value, __viaftp.set, None, 'If true, then resulting snapshot data is fetched by the client via FTP')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __viaftp.name() : __viaftp
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Request a full snapshot of current database"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 139, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute viaftp uses Python identifier viaftp
    __viaftp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'viaftp'), 'viaftp', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON__viaftp', pyxb.binding.datatypes.boolean, unicode_default='false')
    __viaftp._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 140, 6)
    __viaftp._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 140, 6)
    
    viaftp = property(__viaftp.value, __viaftp.set, None, 'If true, then resulting snapshot data is fetched by the client via FTP')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __viaftp.name() : __viaftp
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Push Ports Schema"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 103, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}QueryTimetable uses Python identifier QueryTimetable
    __QueryTimetable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'QueryTimetable'), 'QueryTimetable', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16QueryTimetable', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 105, 4), )

    
    QueryTimetable = property(__QueryTimetable.value, __QueryTimetable.set, None, 'Query for the current timetable ID')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}TimeTableId uses Python identifier TimeTableId
    __TimeTableId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeTableId'), 'TimeTableId', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16TimeTableId', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 110, 4), )

    
    TimeTableId = property(__TimeTableId.value, __TimeTableId.set, None, 'Response for the current timetable ID')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}GetSnapshotReq uses Python identifier GetSnapshotReq
    __GetSnapshotReq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GetSnapshotReq'), 'GetSnapshotReq', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16GetSnapshotReq', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 123, 4), )

    
    GetSnapshotReq = property(__GetSnapshotReq.value, __GetSnapshotReq.set, None, 'Request a standard snapshot of current database')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}GetFullSnapshotReq uses Python identifier GetFullSnapshotReq
    __GetFullSnapshotReq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GetFullSnapshotReq'), 'GetFullSnapshotReq', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16GetFullSnapshotReq', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 135, 4), )

    
    GetFullSnapshotReq = property(__GetFullSnapshotReq.value, __GetFullSnapshotReq.set, None, 'Request a full snapshot of current database')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}SnapshotId uses Python identifier SnapshotId
    __SnapshotId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SnapshotId'), 'SnapshotId', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16SnapshotId', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 147, 4), )

    
    SnapshotId = property(__SnapshotId.value, __SnapshotId.set, None, 'Defines an ID for recovering snapshot data via FTP')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}StartUpdateReq uses Python identifier StartUpdateReq
    __StartUpdateReq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartUpdateReq'), 'StartUpdateReq', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16StartUpdateReq', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 152, 4), )

    
    StartUpdateReq = property(__StartUpdateReq.value, __StartUpdateReq.set, None, 'Start sending available updates.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}StopUpdateReq uses Python identifier StopUpdateReq
    __StopUpdateReq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StopUpdateReq'), 'StopUpdateReq', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16StopUpdateReq', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 157, 4), )

    
    StopUpdateReq = property(__StopUpdateReq.value, __StopUpdateReq.set, None, 'Stop sending available updates.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}FailureResp uses Python identifier FailureResp
    __FailureResp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FailureResp'), 'FailureResp', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16FailureResp', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 162, 4), )

    
    FailureResp = property(__FailureResp.value, __FailureResp.set, None, 'Failure Response')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}uR uses Python identifier uR
    __uR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uR'), 'uR', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16uR', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 183, 4), )

    
    uR = property(__uR.value, __uR.set, None, 'Update Response')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/v16}sR uses Python identifier sR
    __sR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sR'), 'sR', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_httpwww_thalesgroup_comrttiPushPortv16sR', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 209, 4), )

    
    sR = property(__sR.value, __sR.set, None, 'Snapshot Response')

    
    # Attribute ts uses Python identifier ts
    __ts = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ts'), 'ts', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_ts', _ImportedBinding__ct.RTTIDateTimeType, required=True)
    __ts._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 215, 3)
    __ts._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 215, 3)
    
    ts = property(__ts.value, __ts.set, None, 'Local Timestamp')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_2_version', pyxb.binding.datatypes.string, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 220, 3)
    __version._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 220, 3)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __QueryTimetable.name() : __QueryTimetable,
        __TimeTableId.name() : __TimeTableId,
        __GetSnapshotReq.name() : __GetSnapshotReq,
        __GetFullSnapshotReq.name() : __GetFullSnapshotReq,
        __SnapshotId.name() : __SnapshotId,
        __StartUpdateReq.name() : __StartUpdateReq,
        __StopUpdateReq.name() : __StopUpdateReq,
        __FailureResp.name() : __FailureResp,
        __uR.name() : __uR,
        __sR.name() : __sR
    })
    _AttributeMap.update({
        __ts.name() : __ts,
        __version.name() : __version
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Response for the current timetable ID"""
    _TypeDefinition = _ImportedBinding__ct.TimetableIDType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 114, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__ct.TimetableIDType
    
    # Attribute ttfile uses Python identifier ttfile
    __ttfile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ttfile'), 'ttfile', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_3_ttfile', _ImportedBinding__ct.TimetableFilenameType)
    __ttfile._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 117, 8)
    __ttfile._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 117, 8)
    
    ttfile = property(__ttfile.value, __ttfile.set, None, None)

    
    # Attribute ttreffile uses Python identifier ttreffile
    __ttreffile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ttreffile'), 'ttreffile', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_3_ttreffile', _ImportedBinding__ct.TimetableFilenameType)
    __ttreffile._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 118, 8)
    __ttreffile._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 118, 8)
    
    ttreffile = property(__ttreffile.value, __ttreffile.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ttfile.name() : __ttfile,
        __ttreffile.name() : __ttreffile
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (DataResponse):
    """Update Response"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 187, 5)
    _ElementMap = DataResponse._ElementMap.copy()
    _AttributeMap = DataResponse._AttributeMap.copy()
    # Base type is DataResponse
    
    # Element schedule ({http://www.thalesgroup.com/rtti/PushPort/v16}schedule) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element deactivated ({http://www.thalesgroup.com/rtti/PushPort/v16}deactivated) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element association ({http://www.thalesgroup.com/rtti/PushPort/v16}association) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element scheduleFormations ({http://www.thalesgroup.com/rtti/PushPort/v16}scheduleFormations) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element TS ({http://www.thalesgroup.com/rtti/PushPort/v16}TS) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element formationLoading ({http://www.thalesgroup.com/rtti/PushPort/v16}formationLoading) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element OW ({http://www.thalesgroup.com/rtti/PushPort/v16}OW) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element trainAlert ({http://www.thalesgroup.com/rtti/PushPort/v16}trainAlert) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element trainOrder ({http://www.thalesgroup.com/rtti/PushPort/v16}trainOrder) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element trackingID ({http://www.thalesgroup.com/rtti/PushPort/v16}trackingID) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Element alarm ({http://www.thalesgroup.com/rtti/PushPort/v16}alarm) inherited from {http://www.thalesgroup.com/rtti/PushPort/v16}DataResponse
    
    # Attribute updateOrigin uses Python identifier updateOrigin
    __updateOrigin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'updateOrigin'), 'updateOrigin', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_4_updateOrigin', pyxb.binding.datatypes.string)
    __updateOrigin._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 190, 8)
    __updateOrigin._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 190, 8)
    
    updateOrigin = property(__updateOrigin.value, __updateOrigin.set, None, 'A string describing the type of system that originated this update, e.g. "CIS" or "Darwin".')

    
    # Attribute requestSource uses Python identifier requestSource
    __requestSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestSource'), 'requestSource', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_4_requestSource', _ImportedBinding__ct.SourceTypeInst)
    __requestSource._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 195, 8)
    __requestSource._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 195, 8)
    
    requestSource = property(__requestSource.value, __requestSource.set, None, 'The source instance that generated this update, usually a CIS instance.')

    
    # Attribute requestID uses Python identifier requestID
    __requestID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestID'), 'requestID', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_4_requestID', _ImportedBinding__ct.DCISRequestID)
    __requestID._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 200, 8)
    __requestID._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 200, 8)
    
    requestID = property(__requestID.value, __requestID.set, None, 'The DCISRequestID value provided by the originator of this update. Used in conjunction with the requestSource attribute to ensure uniqueness')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __updateOrigin.name() : __updateOrigin,
        __requestSource.name() : __requestSource,
        __requestID.name() : __requestID
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_5 (_ImportedBinding__status.StatusType):
    """Failure Response"""
    _TypeDefinition = _ImportedBinding__status.ErrorMsgType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 166, 5)
    _ElementMap = _ImportedBinding__status.StatusType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__status.StatusType._AttributeMap.copy()
    # Base type is _ImportedBinding__status.StatusType
    
    # Attribute code inherited from {http://thalesgroup.com/RTTI/PushPortStatus/root_1}StatusType
    
    # Attribute requestSource uses Python identifier requestSource
    __requestSource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestSource'), 'requestSource', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_5_requestSource', _ImportedBinding__ct.SourceTypeInst)
    __requestSource._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 169, 8)
    __requestSource._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 169, 8)
    
    requestSource = property(__requestSource.value, __requestSource.set, None, 'The DCIS source that generated this update')

    
    # Attribute requestID uses Python identifier requestID
    __requestID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requestID'), 'requestID', '__httpwww_thalesgroup_comrttiPushPortv16_CTD_ANON_5_requestID', _ImportedBinding__ct.DCISRequestID)
    __requestID._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 174, 8)
    __requestID._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 174, 8)
    
    requestID = property(__requestID.value, __requestID.set, None, 'The DCISRequestID value provided by the originator of this update. Used in conjunction with the updateSource attribute to ensure uniqueness')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __requestSource.name() : __requestSource,
        __requestID.name() : __requestID
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


Pport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pport'), CTD_ANON_2, documentation='Push Ports Schema', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 99, 1))
Namespace.addCategoryObject('elementBinding', Pport.name().localName(), Pport)



DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'schedule'), _ImportedBinding__sch3.Schedule, scope=DataResponse, documentation='Train Schedule', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 41, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'deactivated'), _ImportedBinding__sch2.DeactivatedSchedule, scope=DataResponse, documentation='Notification that a Train Schedule is now deactivated in Darwin.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 46, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'association'), _ImportedBinding__sch2.Association, scope=DataResponse, documentation='Association between schedules', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 51, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleFormations'), _ImportedBinding__fm2.ScheduleFormations, scope=DataResponse, documentation='Train Formation', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 56, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TS'), _ImportedBinding__for.TS, scope=DataResponse, documentation='Train Status', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 61, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'formationLoading'), _ImportedBinding__fm.Loading, scope=DataResponse, documentation='Train Loading', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 66, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OW'), _ImportedBinding__sm.StationMessage, scope=DataResponse, documentation='Darwin Workstation Station Message', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 71, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trainAlert'), _ImportedBinding__ta.TrainAlert, scope=DataResponse, documentation='Train Alert', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 76, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trainOrder'), _ImportedBinding__tor.TrainOrder, scope=DataResponse, documentation='The order that trains are expected to call/pass a particular station platform', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 81, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trackingID'), _ImportedBinding__td.TrackingID, scope=DataResponse, documentation='Indicate a corrected Tracking ID (headcode) for a service in a TD berth.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 86, 3)))

DataResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'alarm'), _ImportedBinding__alm.RTTIAlarm, scope=DataResponse, documentation='A Darwin alarm', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 91, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 41, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 46, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 51, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 56, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 61, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 66, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 71, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 76, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 81, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 86, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 91, 3))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'schedule')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 41, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deactivated')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 46, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'association')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 51, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleFormations')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 56, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TS')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 61, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'formationLoading')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 66, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OW')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 71, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainAlert')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 76, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainOrder')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 81, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trackingID')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 86, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(DataResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alarm')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 91, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DataResponse._Automaton = _BuildAutomaton()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QueryTimetable'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_2, documentation='Query for the current timetable ID', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 105, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeTableId'), CTD_ANON_3, scope=CTD_ANON_2, documentation='Response for the current timetable ID', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 110, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetSnapshotReq'), CTD_ANON, scope=CTD_ANON_2, documentation='Request a standard snapshot of current database', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 123, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetFullSnapshotReq'), CTD_ANON_, scope=CTD_ANON_2, documentation='Request a full snapshot of current database', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 135, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SnapshotId'), _ImportedBinding__ct.SnapshotIDType, scope=CTD_ANON_2, documentation='Defines an ID for recovering snapshot data via FTP', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 147, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartUpdateReq'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_2, documentation='Start sending available updates.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 152, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StopUpdateReq'), pyxb.binding.datatypes.anyType, scope=CTD_ANON_2, documentation='Stop sending available updates.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 157, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FailureResp'), CTD_ANON_5, scope=CTD_ANON_2, documentation='Failure Response', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 162, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uR'), CTD_ANON_4, scope=CTD_ANON_2, documentation='Update Response', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 183, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sR'), DataResponse, scope=CTD_ANON_2, documentation='Snapshot Response', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 209, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'QueryTimetable')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 105, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeTableId')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 110, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GetSnapshotReq')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 123, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GetFullSnapshotReq')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 135, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SnapshotId')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 147, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartUpdateReq')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 152, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StopUpdateReq')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 157, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FailureResp')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 162, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uR')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 183, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sR')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 209, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 41, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 46, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 51, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 56, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 61, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 66, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 71, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 76, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 81, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 86, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 91, 3))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'schedule')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 41, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'deactivated')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 46, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'association')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 51, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleFormations')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 56, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TS')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 61, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'formationLoading')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 66, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OW')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 71, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainAlert')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 76, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trainOrder')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 81, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trackingID')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 86, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'alarm')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchema_v16.xsd', 91, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_2()

