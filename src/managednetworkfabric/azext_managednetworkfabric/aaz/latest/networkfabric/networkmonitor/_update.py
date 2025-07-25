# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkfabric networkmonitor update",
)
class Update(AAZCommand):
    """Update to update certain properties of the NetworkMonitor resource.

    :example: Update the Network Monitor
        az networkfabric networkmonitor update --network-monitor-name example-nm --resource-group example-rg --bmp-configuration '{"stationConfigurationState":"Enabled","scopeResourceId":"/subscriptions/1234ABCD-0A1B-1234-5678-123456ABCDEF/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/networkFabrics/example-fabric","stationName":"name","stationIp":"10.0.0.1","stationPort":62695,"stationConnectionMode":"Active","stationConnectionProperties":{"keepaliveIdleTime":49,"probeInterval":3558,"probeCount":45},"stationNetwork":"/subscriptions/1234ABCD-0A1B-1234-5678-123456ABCDEF/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/example-l3domain/internalNetworks/example-internalnetwork","monitoredNetworks":["/subscriptions/1234ABCD-0A1B-1234-5678-123456ABCDEF/resourceGroups/example-rg/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/example-l3domain"],"exportPolicy":"All","monitoredAddressFamilies":["All"]}'

    :example: Help text for sub parameters under the specific parent can be viewed by using the shorthand syntax '??'. See https://github.com/Azure/azure-cli/tree/dev/doc/shorthand_syntax.md for more about shorthand syntax.
        az networkfabric networkmonitor update --bmp-configuration "??"
        az networkfabric networkmonitor update --bmp-configuration "{exportPolicy: ??"
    """

    _aaz_info = {
        "version": "2024-06-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/networkmonitors/{}", "2024-06-15-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.network_monitor_name = AAZStrArg(
            options=["-n", "--name", "--network-monitor-name"],
            help="Name of the Network Monitor.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z]{1}[a-zA-Z0-9-_]{2,127}$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.bmp_configuration = AAZObjectArg(
            options=["--bmp-configuration"],
            arg_group="Properties",
            help="BGP Monitoring Protocol (BMP) Configurations for the Network Monitor.",
            nullable=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Properties",
            help="Resource tags.",
        )

        bmp_configuration = cls._args_schema.bmp_configuration
        bmp_configuration.export_policy = AAZStrArg(
            options=["export-policy"],
            help="Export Policy for the BMP Configuration.",
            enum={"All": "All", "Post-Policy": "Post-Policy", "Pre-Policy": "Pre-Policy"},
        )
        bmp_configuration.monitored_address_families = AAZListArg(
            options=["monitored-address-families"],
            help="Monitored Address Families for the BMP Configuration.",
        )
        bmp_configuration.monitored_networks = AAZListArg(
            options=["monitored-networks"],
            help="The List of Network ID's that need to be monitored.",
        )
        bmp_configuration.scope_resource_id = AAZResourceIdArg(
            options=["scope-resource-id"],
            help="Scope resource ARM Identifier.",
        )
        bmp_configuration.station_configuration_state = AAZStrArg(
            options=["station-configuration-state"],
            help="Enabling a station. Either True/False.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        bmp_configuration.station_connection_mode = AAZStrArg(
            options=["station-connection-mode"],
            help="Station Connection Mode.",
            enum={"Active": "Active", "Passive": "Passive"},
        )
        bmp_configuration.station_connection_properties = AAZObjectArg(
            options=["station-connection-properties"],
            help="Station Connection Properties.",
        )
        bmp_configuration.station_ip = AAZStrArg(
            options=["station-ip"],
            help="IP Address of the station.",
        )
        bmp_configuration.station_name = AAZStrArg(
            options=["station-name"],
            help="Name of the station.",
        )
        bmp_configuration.station_network = AAZResourceIdArg(
            options=["station-network"],
            help="Network of the station",
        )
        bmp_configuration.station_port = AAZIntArg(
            options=["station-port"],
            help="Port of the station. Default value is 5000.",
            fmt=AAZIntArgFormat(
                maximum=65535,
                minimum=1,
            ),
        )

        monitored_address_families = cls._args_schema.bmp_configuration.monitored_address_families
        monitored_address_families.Element = AAZStrArg(
            enum={"All": "All", "ipv4Unicast": "ipv4Unicast", "ipv6Unicast": "ipv6Unicast", "vpnIpv4": "vpnIpv4", "vpnIpv6": "vpnIpv6"},
        )

        monitored_networks = cls._args_schema.bmp_configuration.monitored_networks
        monitored_networks.Element = AAZResourceIdArg()

        station_connection_properties = cls._args_schema.bmp_configuration.station_connection_properties
        station_connection_properties.keepalive_idle_time = AAZIntArg(
            options=["keepalive-idle-time"],
            help="Connection keepalive idle time in seconds",
            fmt=AAZIntArgFormat(
                maximum=3600,
                minimum=1,
            ),
        )
        station_connection_properties.probe_count = AAZIntArg(
            options=["probe-count"],
            help="Probe count, default value is 10",
            fmt=AAZIntArgFormat(
                maximum=100,
                minimum=1,
            ),
        )
        station_connection_properties.probe_interval = AAZIntArg(
            options=["probe-interval"],
            help="Probe interval in seconds, default value is 60",
            fmt=AAZIntArgFormat(
                maximum=3600,
                minimum=1,
            ),
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.NetworkMonitorsUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetworkMonitorsUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkMonitors/{networkMonitorName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkMonitorName", self.ctx.args.network_monitor_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-06-15-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType)
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("bmpConfiguration", AAZObjectType, ".bmp_configuration", typ_kwargs={"nullable": True})

            bmp_configuration = _builder.get(".properties.bmpConfiguration")
            if bmp_configuration is not None:
                bmp_configuration.set_prop("exportPolicy", AAZStrType, ".export_policy")
                bmp_configuration.set_prop("monitoredAddressFamilies", AAZListType, ".monitored_address_families")
                bmp_configuration.set_prop("monitoredNetworks", AAZListType, ".monitored_networks")
                bmp_configuration.set_prop("scopeResourceId", AAZStrType, ".scope_resource_id")
                bmp_configuration.set_prop("stationConfigurationState", AAZStrType, ".station_configuration_state")
                bmp_configuration.set_prop("stationConnectionMode", AAZStrType, ".station_connection_mode")
                bmp_configuration.set_prop("stationConnectionProperties", AAZObjectType, ".station_connection_properties")
                bmp_configuration.set_prop("stationIp", AAZStrType, ".station_ip")
                bmp_configuration.set_prop("stationName", AAZStrType, ".station_name")
                bmp_configuration.set_prop("stationNetwork", AAZStrType, ".station_network")
                bmp_configuration.set_prop("stationPort", AAZIntType, ".station_port")

            monitored_address_families = _builder.get(".properties.bmpConfiguration.monitoredAddressFamilies")
            if monitored_address_families is not None:
                monitored_address_families.set_elements(AAZStrType, ".")

            monitored_networks = _builder.get(".properties.bmpConfiguration.monitoredNetworks")
            if monitored_networks is not None:
                monitored_networks.set_elements(AAZStrType, ".")

            station_connection_properties = _builder.get(".properties.bmpConfiguration.stationConnectionProperties")
            if station_connection_properties is not None:
                station_connection_properties.set_prop("keepaliveIdleTime", AAZIntType, ".keepalive_idle_time")
                station_connection_properties.set_prop("probeCount", AAZIntType, ".probe_count")
                station_connection_properties.set_prop("probeInterval", AAZIntType, ".probe_interval")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.annotation = AAZStrType()
            properties.bmp_configuration = AAZObjectType(
                serialized_name="bmpConfiguration",
            )
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.last_operation = AAZObjectType(
                serialized_name="lastOperation",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            bmp_configuration = cls._schema_on_200.properties.bmp_configuration
            bmp_configuration.export_policy = AAZStrType(
                serialized_name="exportPolicy",
            )
            bmp_configuration.monitored_address_families = AAZListType(
                serialized_name="monitoredAddressFamilies",
            )
            bmp_configuration.monitored_networks = AAZListType(
                serialized_name="monitoredNetworks",
            )
            bmp_configuration.scope_resource_id = AAZStrType(
                serialized_name="scopeResourceId",
            )
            bmp_configuration.station_configuration_state = AAZStrType(
                serialized_name="stationConfigurationState",
            )
            bmp_configuration.station_connection_mode = AAZStrType(
                serialized_name="stationConnectionMode",
            )
            bmp_configuration.station_connection_properties = AAZObjectType(
                serialized_name="stationConnectionProperties",
            )
            bmp_configuration.station_ip = AAZStrType(
                serialized_name="stationIp",
            )
            bmp_configuration.station_name = AAZStrType(
                serialized_name="stationName",
            )
            bmp_configuration.station_network = AAZStrType(
                serialized_name="stationNetwork",
            )
            bmp_configuration.station_port = AAZIntType(
                serialized_name="stationPort",
            )

            monitored_address_families = cls._schema_on_200.properties.bmp_configuration.monitored_address_families
            monitored_address_families.Element = AAZStrType()

            monitored_networks = cls._schema_on_200.properties.bmp_configuration.monitored_networks
            monitored_networks.Element = AAZStrType()

            station_connection_properties = cls._schema_on_200.properties.bmp_configuration.station_connection_properties
            station_connection_properties.keepalive_idle_time = AAZIntType(
                serialized_name="keepaliveIdleTime",
            )
            station_connection_properties.probe_count = AAZIntType(
                serialized_name="probeCount",
            )
            station_connection_properties.probe_interval = AAZIntType(
                serialized_name="probeInterval",
            )

            last_operation = cls._schema_on_200.properties.last_operation
            last_operation.details = AAZStrType(
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _UpdateHelper:
    """Helper class for Update"""


__all__ = ["Update"]
