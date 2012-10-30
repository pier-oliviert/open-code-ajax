<?php

namespace OC\TodoBundle\Entity;

use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

/**
 * OC\TodoBundle\Entity\Todo
 *
 * @ORM\Entity
 */
class Todo
{
    /**
     * @var integer $id
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
     * @var string $title
     *
     * @Assert\MinLength(3)
     * @ORM\Column(name="title", type="string", length=255)
     */
    private $title;

    /**
     * @var boolean $done
     *
     * @ORM\Column(name="done", type="boolean")
     */
    private $done = false;


    /**
     * Get id
     *
     * @return integer 
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set title
     *
     * @param string $title
     * @return Todo
     */
    public function setTitle($title)
    {
        $this->title = $title;
    
        return $this;
    }

    /**
     * Get title
     *
     * @return string 
     */
    public function getTitle()
    {
        return $this->title;
    }

    /**
     * Set done
     *
     * @param boolean $done
     * @return Todo
     */
    public function setDone($done)
    {
        $this->done = $done;
    
        return $this;
    }

    /**
     * Get done
     *
     * @return boolean 
     */
    public function getDone()
    {
        return $this->done;
    }
}