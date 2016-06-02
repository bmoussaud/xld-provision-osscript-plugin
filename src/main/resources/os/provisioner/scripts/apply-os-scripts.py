import com.xebialabs.xldeploy.provisioner.host.LazyHost as LazyHost

provisioners = filter(lambda provisioner: provisioner.type == "os.provisioner.ExecutedScript", deployed.provisioners)

for p in puppet_provisioners:
    host = wrap(LazyHost())
    host.setHostTemplate(p.deployable.hostTemplate)
    host.setProvisionedBlueprint(deployedApplication)
    host.setSourceProvisioned(deployed)
    step = steps.os_script(script="os/provisioner/run-script",
            target_host=host,
            order = 68,
            upload_artifacts = True,
            freemarker_context = {'scripted': p},
            description="Provision {0} instance with the os script provisioner {1} using script file {2}".format( deployed.name, p.name, p.file.name))
    context.addStep(step)
