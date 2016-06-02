import com.xebialabs.xldeploy.provisioner.host.LazyHost as LazyHost

puppet_provisioners = filter(lambda provisioner: provisioner.type == "puppet.provisioner.AppliedManifest", deployed.provisioners)

for p in puppet_provisioners:
    host = wrap(LazyHost())
    host.setHostTemplate(p.deployable.hostTemplate)
    host.setProvisionedBlueprint(deployedApplication)
    host.setSourceProvisioned(deployed)
    step = steps.puppet_apply_manifest(targetHost=host,
                                       manifest=p,
                                       description="Provision {0} instance with puppet provisioner {1} using manifest file {2}".format(
                                           deployed.name,
                                           p.name, p.file.name))
    context.addStep(step)