"""An Azure RM Python Pulumi program"""


import pulumi
import pulumi_azure_native as azure_native

#%%%%%%%%%%%%%%
resource_group = azure_native.resources.ResourceGroup('resource_group', 
    resource_group_name='Work')


storage_account = azure_native.storage.StorageAccount("storage_account",
    access_tier=azure_native.storage.AccessTier.HOT,
    account_name="gasdata",
    allow_blob_public_access=False,
    allow_cross_tenant_replication=False,
    allow_shared_key_access=True,
    default_to_o_auth_authentication=False,
    dns_endpoint_type="Standard",
    enable_https_traffic_only=True,
    encryption=azure_native.storage.EncryptionArgs(
        key_source="Microsoft.Storage",
        require_infrastructure_encryption=False,
        services=azure_native.storage.EncryptionServicesArgs(
            blob=azure_native.storage.EncryptionServiceArgs(
                enabled=True,
                key_type="Account",
            ),
            file=azure_native.storage.EncryptionServiceArgs(
                enabled=True,
                key_type="Account",
            ),
        ),
    ),
    kind="StorageV2",
    location="uaenorth",
    minimum_tls_version="TLS1_2",
    network_rule_set=azure_native.storage.NetworkRuleSetArgs(
        bypass="AzureServices",
        default_action=azure_native.storage.DefaultAction.ALLOW,
    ),
    public_network_access="Enabled",
    resource_group_name="Work",
    sku=azure_native.storage.SkuArgs(
        name="Standard_RAGRS",
    ),
    opts=pulumi.ResourceOptions(protect=True))


# Create an Azure Function App

app_service_plan = azure_native.web.AppServicePlan("app_service_plan",
    elastic_scale_enabled=False,
    hyper_v=False,
    is_spot=False,
    is_xenon=False,
    kind="functionapp",
    location="UAE North",
    maximum_elastic_worker_count=1,
    name="ASP-Work-bd74",
    per_site_scaling=False,
    reserved=True,
    resource_group_name="Work",
    sku=azure_native.web.SkuDescriptionArgs(
        capacity=0,
        family="Y",
        name="Y1",
        size="Y1",
        tier="Dynamic",
    ),
    target_worker_count=0,
    target_worker_size_id=0,
    zone_redundant=False,
    opts=pulumi.ResourceOptions(protect=True))


function_app = azure_native.web.WebApp("function_app",
    client_affinity_enabled=False,
    client_cert_enabled=False,
    client_cert_mode=azure_native.web.ClientCertMode.REQUIRED,
    container_size=1536,
    custom_domain_verification_id="43ED0F8881BBD26800B141E7A15CFB7F5D48A7DE4DA2897102B890FCC9273768",
    daily_memory_time_quota=0,
    enabled=True,
    host_name_ssl_states=[
        azure_native.web.HostNameSslStateArgs(
            host_type=azure_native.web.HostType.STANDARD,
            name="ahmadtimetriggerfunction.azurewebsites.net",
            ssl_state=azure_native.web.SslState.DISABLED,
        ),
        azure_native.web.HostNameSslStateArgs(
            host_type=azure_native.web.HostType.REPOSITORY,
            name="ahmadtimetriggerfunction.scm.azurewebsites.net",
            ssl_state=azure_native.web.SslState.DISABLED,
        ),
    ],
    host_names_disabled=False,
    https_only=True,
    hyper_v=False,
    is_xenon=False,
    key_vault_reference_identity="SystemAssigned",
    kind="functionapp,linux",
    location="UAE North",
    name="ahmadtimetriggerfunction",
    public_network_access="Enabled",
    redundancy_mode=azure_native.web.RedundancyMode.NONE,
    reserved=True,
    resource_group_name="Work",
    scm_site_also_stopped=False,
    server_farm_id="/subscriptions/79dea4cb-451a-46b7-a381-a6f48240a0b7/resourceGroups/Work/providers/Microsoft.Web/serverfarms/ASP-Work-bd74",
    site_config=azure_native.web.SiteConfigArgs(
        acr_use_managed_identity_creds=False,
        always_on=False,
        function_app_scale_limit=200,
        http20_enabled=False,
        linux_fx_version="Python|3.11",
        minimum_elastic_instance_count=0,
        number_of_workers=1,
    ),
    storage_account_required=False,
    vnet_content_share_enabled=False,
    vnet_image_pull_enabled=False,
    vnet_route_all_enabled=False,
    opts=pulumi.ResourceOptions(protect=True))

# Create an Azure Virtual Network
virtual_network = azure_native.network.VirtualNetwork("virtual_network",
    address_space=azure_native.network.AddressSpaceArgs(
        address_prefixes=["10.0.0.0/16"],
    ),
    enable_ddos_protection=False,
    location="uaenorth",
    resource_group_name="Work",
    subnets=[azure_native.network.SubnetArgs(
        address_prefix="10.0.0.0/24",
        id="/subscriptions/79dea4cb-451a-46b7-a381-a6f48240a0b7/resourceGroups/Work/providers/Microsoft.Network/virtualNetworks/LNG-vnet/subnets/default",
        name="default",
        private_endpoint_network_policies="Disabled",
        private_link_service_network_policies="Enabled",
        type="Microsoft.Network/virtualNetworks/subnets",
    )],
    virtual_network_name="LNG-vnet",
    opts=pulumi.ResourceOptions(protect=True))

# Create an Azure Network Security Group
nsg = azure_native.network.NetworkSecurityGroup("nsg",
    location="uaenorth",
    network_security_group_name="High-Performance-CPU-nsg",
    resource_group_name="Work",
    security_rules=[azure_native.network.SecurityRuleArgs(
        access="Allow",
        destination_address_prefix="*",
        destination_port_range="3389",
        direction="Inbound",
        id="/subscriptions/79dea4cb-451a-46b7-a381-a6f48240a0b7/resourceGroups/Work/providers/Microsoft.Network/networkSecurityGroups/High-Performance-CPU-nsg/securityRules/RDP",
        name="RDP",
        priority=300,
        protocol="TCP",
        source_address_prefix="*",
        source_port_range="*",
        type="Microsoft.Network/networkSecurityGroups/securityRules",
    )],
    opts=pulumi.ResourceOptions(protect=True))

# Create an Azure Public IP Address
public_ip = azure_native.network.PublicIPAddress("public_ip",
    idle_timeout_in_minutes=4,
    ip_address="20.203.45.137",
    location="uaenorth",
    public_ip_address_version="IPv4",
    public_ip_allocation_method="Static",
    public_ip_address_name="High-Performance-CPU-ip",
    resource_group_name="Work",
    sku=azure_native.network.PublicIPAddressSkuArgs(
        name="Standard",
        tier="Regional",
    ),
    opts=pulumi.ResourceOptions(protect=True))

# Create an Azure SQL Server

sql_server = azure_native.sql.Server("sql_server",
    administrator_login="ahmadriad",
    administrators=azure_native.sql.ServerExternalAdministratorArgs(
        administrator_type="ActiveDirectory",
        azure_ad_only_authentication=False,
        login="aaahmad15@eng.just.edu.jo",
        principal_type="User",
        sid="1af9c490-7adc-4d2a-8bc8-f8fa05b1849c",
        tenant_id="13e5772d-fae9-4291-8e92-3ee771b9ec38",
    ),
    location="uaenorth",
    minimal_tls_version="1.2",
    public_network_access="Enabled",
    resource_group_name="Work",
    restrict_outbound_network_access="Disabled",
    server_name="ahmad1997",
    version="12.0",
    opts=pulumi.ResourceOptions(protect=True))

# Create an Azure SQL Database
sql_database = azure_native.sql.Database("sql_database",
    auto_pause_delay=60,
    catalog_collation="SQL_Latin1_General_CP1_CI_AS",
    collation="SQL_Latin1_General_CP1_CI_AS",
    database_name="scrapeddata",
    is_ledger_on=False,
    location="uaenorth",
    maintenance_configuration_id="/subscriptions/79dea4cb-451a-46b7-a381-a6f48240a0b7/providers/Microsoft.Maintenance/publicMaintenanceConfigurations/SQL_Default",
    max_size_bytes=34359738368,
    min_capacity=0.5,
    read_scale="Disabled",
    requested_backup_storage_redundancy="Local",
    resource_group_name="Work",
    server_name="ahmad1997",
    sku=azure_native.sql.SkuArgs(
        capacity=1,
        family="Gen5",
        name="GP_S_Gen5",
        tier="GeneralPurpose",
    ),
    zone_redundant=False,
    opts=pulumi.ResourceOptions(protect=True))




# Output the endpoint of the Function App
pulumi.export('function_app_endpoint', function_app.default_host_name)

































