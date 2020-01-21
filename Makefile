.PONY: deploy-call-function, deploy-message-container, register-image


deploy-call-function:
	gcloud functions deploy alarm_call \
					--runtime python37 \
					--source functions \
					--entry-point alarm_call_pubsub \
					--trigger-topic start_call \
					--timeout 540

deploy-message-container:

register-image:
