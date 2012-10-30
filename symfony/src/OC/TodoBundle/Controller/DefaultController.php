<?php

namespace OC\TodoBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Method;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;

use OC\TodoBundle\Entity\Todo;

class DefaultController extends Controller
{
	/**
	 * @Route("/", name="todos")
	 *
	 */
    public function indexAction()
    {
        $repositery = $this->getDoctrine()
            ->getRepository('TodoBundle:Todo');
        
        $query = $repositery->createQueryBuilder('t')
            ->where('t.done = FALSE')
            ->getQuery();
        
        $todos = $query->getResult();

        $form = $this->createFormBuilder(new Todo())
        ->add("title", "text")
        ->getForm();

        return $this->render('TodoBundle:Default:index.html.twig', 
            array(
                'todos' => $todos,
                'form' => $form->createView(),
                )
            );
    }

    /**
     * @Route("/todo", name="create_todo")
     * @Method({"POST"})
     */
    public function createAction(Request $request)
    {
        $todo = new Todo();

        $form = $this->createFormBuilder( $todo )
            ->add("title", "text")
            ->getForm();

        $form->bind($request);

        if ($form->isValid()) {
            $em = $this->getDoctrine()->getManager();
            $em->persist($todo);
            $em->flush();
        }

        if ($request->isXmlHttpRequest()) {
            $response = $this->render('TodoBundle:Default:create.js.twig', 
                array(
                    'todo' => $todo,
                    'form' => $form,
                    )
            );

            $response->headers->set("Content-Type", "text/javascript");
            return $response;
        }
        else {
            return $this->redirect($this->generateUrl('todos'));
        }
    }

	/**
     * @Route("/todo/{id}/done", name="finish_todo")
     * @Method({"GET"})
     */
    public function finishAction($id, Request $request)
    {
        $em = $this->getDoctrine()->getManager();
        $todo = $em->getRepository("TodoBundle:Todo")
            ->find($id);

        if ($todo) {
            $todo->setDone(True);
            $em->flush();
        }

        if ($request->isXmlHttpRequest()) {
            $response = $this->render('TodoBundle:Default:update.js.twig',
                array(
                    'todo' => $todo
                    )
                );
            $response->headers->set("Content-Type", "text/javascript");
            return $response;
        }
        return $this->redirect($this->generateUrl('todos'));
    }

}
