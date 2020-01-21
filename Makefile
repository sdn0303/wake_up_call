.PONY: deploy-call-message-function, deploy-wake-up-call-function

deploy-call-message-function:
	gcloud functions deploy call-message \
					--runtime python37 \
					--source functions/call_message \
					--entry-point message \
					--trigger-http \
					--timeout 540

deploy-wake-up-call-function:
	gcloud functions deploy wake-up-call \
					--runtime python37 \
					--source functions/wake_up_call \
					--entry-point wake_up_call_pubsub \
					--trigger-topic start-call \
					--timeout 540
