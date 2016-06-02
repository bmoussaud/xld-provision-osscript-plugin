import com.xebialabs.xldeploy.provisioner.host.LazyHost as LazyHost

provisioners = filter(lambda provisioner: provisioner.type == "puppet.provisioner.AppliedManifest", deployed.provisioners)
for p in provisioners:
    host = wrap(LazyHost())
    host.setHostTemplate(p.deployable.hostTemplate)
    host.setProvisionedBlueprint(deployedApplication)
    host.setSourceProvisioned(deployed)
    for module in p.modules:
        if module.moduleName is None:
            moduleName = module.name
        else:
            moduleName = module.moduleName

        step = steps.puppet_install_module(targetHost=host,
                                           module=moduleName,
                                           description="Install puppet module {0} on {1}".format(moduleName, deployed.name))
        context.addStep(step)